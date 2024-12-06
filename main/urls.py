from django.contrib import admin
from django.urls import include, path

import blog
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
]
