from django.contrib import admin
from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('add/', views.add_blog, name='add_blog'),
    path('<int:blog_id>/', views.get_blog, name='get_blog'),
    path('<int:blog_id>/update_name/', views.set_blog_name, name='set_blog_name'),
    path('<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),
    path('<int:blog_id>/name/', views.get_blog_name, name='get_blog_name'),
    path('react/', views.react_to_post, name='react_to_post'),
    path('<int:blog_id>/post/create/', views.add_post, name='add_post'),  
    path('<int:blog_id>/post/<int:post_id>/', views.get_post, name='get_post'), 
]


""" urlpatterns = [
    path('add/', views.add_blog, name='add_blog'),
    path('<int:blog_id>/', views.get_blog, name='get_blog'),
    path('<int:blog_id>/update_name/', views.set_blog_name, name='set_blog_name'),
    path('<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),
    path('<int:blog_id>/name/', views.get_blog_name, name='get_blog_name'),
    path('react/', views.react_to_post, name='react_to_post'),
    path('<int:blog_id>/post/create/', views.add_post, name='add_post'),  
] """