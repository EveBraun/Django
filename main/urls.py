from django.contrib import admin
from django.urls import path
from .views import index, post_list, about, contacts, post_add

app_name = 'main'
urlpatterns = [
    
    path('', index),
    path('posts/', post_list, name='post_list'),
    path('about/', about, name='about'), 
    path('contacts/', contacts, name='contacts'), 
    path('post_add/', post_add, name='post_add'), 
    
]
