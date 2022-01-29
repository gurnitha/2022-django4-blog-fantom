# blog/views.py

# Django modules
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.list import View, ListView

# Locals
from apps.blog.models import Category, Tag, Post 

# Create your views here.

class HomeView(View):

    def get(self, request, *args, **kwargs):
        sliders = Post.objects.filter(post_slider=True)
        first_two_posts = Post.objects.filter(post_status='published', post_slider=False, post_type='featured').order_by('-id')[0:2]
        second_two_posts = Post.objects.filter(post_status='published', post_slider=False, post_type='featured').order_by('-id')[2:4]
        post_small = Post.objects.filter(post_status='published', post_type='small')[0:2]
        context = {
            'posts_slider':sliders,
            'first_two_posts':first_two_posts,
            'second_two_posts':second_two_posts,
            'posts_small':post_small
        }
        return render(request, 'blog/index.html', context)


class PostListView(ListView):

    model = Post 
    paginate_by = 4
    context_object_name = 'post_list'
    template_name = "blog/post_list.html"

    def get_queryset(self):
        return self.model.objects.filter(post_status='published').order_by('-id')


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

