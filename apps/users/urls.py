# users/urls.py

# Django modules
from django.urls import path

# Locals
from .views import *

app_name = 'users'
urlpatterns = [
    # Users: register, login, logout
    path('user/register/', UserRegisterView, name='user_register'),
    path('user/login/', UserLoginView, name='user_login'),
    path('user/logout/', UserLogoutView, name='user_logout'),

    # Users: list, profile
    path('user/list/', UserListView, name='user_list'),
    path('user/profile/', UserProfileView, name='user_profile'),
    path('user/profile-update/', UserProfileUpdateView, name='user_profile_update'),

    # Users: post
    path('user/post/', UserPostView, name='user_post'),
]
