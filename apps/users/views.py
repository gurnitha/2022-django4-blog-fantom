# users/views.py

# Django modules
from django.shortcuts import render

# Locals

# Create your views here.


# USER REGISTER, LOGIN, LOGOUT
# ----------------------------

# View: UserRegisterView
def UserRegisterView(request):
    return render(request, 'users/user_register.html')


# View: UserLoginView
def UserLoginView(request):
    return render(request, 'users/user_login.html')


# View: UserLogoutView
def UserLogoutView(request):
    return render(request, 'users/user_login.html')


# USER LIST, PROFILE
# ----------------------------


# View: UserListView
def UserListView(request):
    return render(request, 'users/user_list.html')


# View: UserProfileView
def UserProfileView(request):
    return render(request, 'users/user_profile.html')


# View: UserProfileUpdateView
def UserProfileUpdateView(request):
    return render(request, 'users/user_profile_update.html')


# USER POSTS
# ----------------------------

# View: UserPostView
def UserPostView(request):
    return render(request, 'users/user_post.html')
