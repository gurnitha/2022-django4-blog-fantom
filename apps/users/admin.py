# users/admin.py

# Django modules
from django.contrib import admin

# Locals
from . models import Profile 

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'name', 'username', 'profile_image',)
	search_fields = ('username',)
