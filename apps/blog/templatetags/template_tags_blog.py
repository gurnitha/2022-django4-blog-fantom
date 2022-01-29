# blog/templatetags/blog_tags.py

# Django modules
from django import template

# Locals
from apps.blog.models import Post 

# Template library
register = template.Library()

# Register your template here.


@register.inclusion_tag('blog/shared/aside_popular_posts.html')
def show_popular_posts(count=5):
	popular_posts = Post.objects.filter(post_status='published', post_type='featured').order_by('-post_view')[:count]
	# print(popular_posts) # It works
	context = {'popular_posts':popular_posts}
	return context