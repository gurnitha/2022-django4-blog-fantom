# blog/views.py

# Django modules
from django.shortcuts import render

# Locals

# Create your views here.

def HomeView(request):
    return render(request, 'blog/index.html')


def PostListView(request):
    return render(request, 'blog/post_list.html')


def PostDetailView(request):
    return render(request, 'blog/post_detail.html')


def PostsByCategoryView(request):
    return render(request, 'blog/posts_by_category.html')


def PostByCategoryDetailView(request):
    return render(request, 'blog/post_by_category_detail.html')


def PostsByTagView(request):
    return render(request, 'blog/posts_by_tag.html')


def PostByTagDetailView(request):
    return render(request, 'blog/post_by_tag_detail.html')


def PostsArchiveView(request):
    return render(request, 'blog/posts_archive.html')


def SearchView(request):
    return render(request, 'blog/search.html')

