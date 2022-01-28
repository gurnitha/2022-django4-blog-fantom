# blog/admin.py

# Django modules
from django.contrib import admin

# Locals
from . models import Category, Tag, Post 

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('cat_name', 'cat_slug')
	search_fields = ('cat_name',)
	prepopulated_fields = {'cat_slug': ('cat_name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('tag_name', 'tag_slug')
	search_fields = ('tag_name',)
	prepopulated_fields = {'tag_slug': ('tag_name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('post_title', 'post_slug', 'post_author', 'post_publish', 'post_status')
	list_filter = ('post_status', 'post_created', 'post_publish', 'post_author')
	search_fields = ('post_title', 'post_content')
	prepopulated_fields = {'post_slug': ('post_title',)}
	raw_id_fields = ('post_author',)
	date_hierarchy = 'post_publish'
	ordering = ('post_status', 'post_publish')