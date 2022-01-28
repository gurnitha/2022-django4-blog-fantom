# blog/urls.py

# Django modules
from django.urls import path

# Locals
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('posts/', PostListView, name='post_list'),
    path('post/1', PostDetailView, name='post_detail'),
    path('categories/', PostsByCategoryView, name='posts_by_category'),
    path('category/1', PostByCategoryDetailView, name='post_by_category_detail'),
    path('tags/', PostsByTagView, name='posts_by_tag'),
    path('tag/1', PostByTagDetailView, name='post_by_tag_detail'),
    path('search/', SearchView, name='search'),
]