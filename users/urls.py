from django.contrib import admin
from django.urls import path

from users import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('registration/', views.registration_view, name='registration_view'),
    path('profile/', views.profile_view, name='profile_view'),
    path('logout/', views.logout_view, name='logout_view'),
]
