from django.contrib import admin
from django.urls import path

from authorization import views

app_name = 'authorization'

urlpatterns = [
    path('', views.index, name='index')
]
