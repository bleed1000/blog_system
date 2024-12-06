from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from users.services.auth_service import AuthService

auth_service = AuthService()

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth_service.login(request, username, password)
            if user:
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = auth_service.register(
                username=form.cleaned_data['username'],
                password1=form.cleaned_data['password1'],
                password2=form.cleaned_data['password2']
            )
            auth_service.login(request, user.username, form.cleaned_data['password1'])
            return HttpResponseRedirect(reverse('user:profile_view'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)

def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            auth_service.update_user(
                user=request.user,
                image=form.cleaned_data.get('image'),
                username=form.cleaned_data.get('username')
            )
            return redirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)



def logout_view(request):
    auth.logout(request)
    return redirect(reverse('main:index'))
