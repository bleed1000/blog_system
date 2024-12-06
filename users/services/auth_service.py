from django.contrib import auth
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404

class AuthService:

    def register(self, username, password1, password2):
        if password1 != password2:
            raise ValueError("Пароли не совпадают")

        user = User.objects.create_user(username=username, password=password1)
        return user

    def login(self, request, username, password):
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return user
        return None

    def update_user(self, user, image=None, username=None):
        if username:
            user.username = username
        if image:
            user.image = image
        user.save()
        return user
