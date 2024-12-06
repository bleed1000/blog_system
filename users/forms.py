from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

from users.models import TextComments, User

class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()

    # username = forms.CharField(
    #     label = 'Имя',
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                   'class': 'input-box',
    #                                   'placeholder': 'Enter your username'}))
    # password = forms.CharField(
    #     label = 'Пароль',
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       'class': 'input-box',
    #                                       'placeholder': 'Enter your password'})
    # )

    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]

class ProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields = [
            'image',
            'username',
        ]

        image = forms.ImageField()
        username = forms.CharField()    


class CommentForm(forms.ModelForm):
    text = forms.CharField()

    class Meta:
        model = TextComments
        fields = ['text']