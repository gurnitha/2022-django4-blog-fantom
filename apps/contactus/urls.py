# contactus/urls.py

# Django modules
from django.urls import path

# Locals
from .views import *

app_name = 'contactus'
urlpatterns = [
    path('contactus/', ContactUsView, name='contactus'),
]
