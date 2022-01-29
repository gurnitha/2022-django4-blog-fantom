# blog/templatetags/blog_tags.py

# Django modules
from django import template

# Locals
from apps.blog.models import Post, Category 

# Template library
register = template.Library()

# Register your template here.


@register.inclusion_tag('blog/shared/aside_popular_posts.html')
def show_popular_posts(count=5):
	popular_posts = Post.objects.filter(post_status='published', post_type='featured').order_by('-post_view')[:count]
	# print(popular_posts) # It works
	context = {'popular_posts':popular_posts}
	return context


@register.inclusion_tag('blog/shared/aside_category.html')
def show_posts_by_category():
	categories = Category.objects.all()
	# print(categories) # It works
	context = {'categories':categories}
	return context

