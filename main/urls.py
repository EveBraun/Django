from django.contrib import admin
from django.urls import path
from .views import index, post_list, about, contacts, post_add, post_detail

app_name = 'main'
urlpatterns = [
    
    path('', index), 
    path('about/', about, name='about'), 
    path('contacts/', contacts, name='contacts'), 

    path('posts/', post_list, name='post_list'),
    path('post_add/', post_add, name='post_add'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),

]
