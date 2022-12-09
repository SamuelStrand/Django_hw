from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    path('', views.home, name=''),
    path('home/', views.home, name=''),
    path('posts/', views.posts, name=''),

]
