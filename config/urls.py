# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Blog
    path('', include('apps.blog.urls', namespace='blog')),
    # Contactus
    path('', include('apps.contactus.urls', namespace='contactus')),
    # Users
    path('', include('apps.users.urls', namespace='users')),
    # Admin
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
