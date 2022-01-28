# blog/views.py

# Django modules
from django.shortcuts import render
from django.views.generic.list import ListView

# Locals
from apps.blog.models import Category, Tag, Post 

# Create your views here.


# GCBV: HomeView
class HomeView(ListView):

    post_model = Post
    context_object_name = 'posts_slider'
    template_name = "blog/index.html"

    # Get all posts with status published
    def get_queryset(self):
        return self.post_model.objects.filter(post_status='published')

    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


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

