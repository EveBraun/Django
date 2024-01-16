from django.contrib import admin
from django.urls import path
from .views import index, post_list

app_name = 'main'
urlpatterns = [
    
    path('', index),
    path('posts/', post_list, name='post_list'),
    
]
