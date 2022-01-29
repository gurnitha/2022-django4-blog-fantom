# blog/views.py

# Django modules
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.list import ListView

# Locals
from apps.blog.models import Category, Tag, Post 

# Create your views here.


class HomeView(ListView):

    model = Post 
    paginate_by = 2
    context_object_name = 'posts'
    template_name = "blog/index.html"

    # Get all posts with status pubish, which will be
    # the FIRST objects to be considered by Django.
    # If you need extra objects, do it in get_context_data
    def get_queryset(self):
        return self.model.objects.filter(post_status='published', post_type='featured')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # context['now'] = timezone.now()
        context['posts_slider'] = Post.objects.all().filter(post_slider=True)
        context['posts_small'] = Post.objects.all().filter(post_status='published', post_type='small')[:2]
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

