# apps/users/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import User

# Locals

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
    	User, 
    	on_delete=models.CASCADE, 
    	null=True, blank=True)
    name = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True)
    username = models.CharField(
        max_length=200, 
        blank=True, 
        null=True)
    bio = models.TextField(
    	blank=True, 
    	null=True)
    profile_image = models.ImageField(
    	null=True, 
    	blank=True, 
    	upload_to='profiles/', 
    	default="profiles/user-default.png")

    def __str__(self):
        return str(self.username)

