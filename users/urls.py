from django.urls import path
from .views import register, log_in, log_out, get_user_info

app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path("user/<int:pk>/", get_user_info, name='user_info'),
]