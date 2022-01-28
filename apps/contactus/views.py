# contactus/views.py

# Django modules
from django.shortcuts import render

# Locals

# Create your views here.

def ContactUsView(request):
    return render(request, 'contactus/contactus.html')
