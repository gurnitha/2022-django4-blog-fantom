# blog/models.py

# Django modules
from django.db import models
from django.utils import timezone

# Locals
from apps.users.models import Profile

# Create your models here.


# MODEL:Category
class Category(models.Model):

    cat_name 	= models.CharField(max_length=255)
    cat_slug  	= models.SlugField(max_length=255, verbose_name='Url', unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['cat_name']

    def __str__(self):
        return self.cat_name

    # Define get_category_absolute_url
    def get_category_absolute_url(self):
        return reverse('blog:posts_by_category', kwargs={'slug':self.slug})


# MODEL:TAG
class Tag(models.Model):

    tag_name 	= models.CharField(max_length=50)
    tag_slug  	= models.SlugField(max_length=255, verbose_name='Url', unique=True)

    class Meta:
        verbose_name_plural = 'Tags'
        ordering = ['tag_name']

    def __str__(self):
        return self.tag_name

    def get_tag_absolute_url(self):
        return reverse('blog:posts_by_tag', kwargs={'slug': self.slug})



# MODEL:Post
class Post(models.Model):

	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)

	POST_TYPE_CHOICES = (
		('unfeatured', 'Unfeatured'),
		('featured', 'Featured'),
	)

	post_title 		= models.CharField(max_length=150)
	post_slug 		= models.SlugField(max_length=250, unique_for_date='post_publish')
	post_author 	= models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='blog_posts')
	post_category 	= models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
	post_tag    	= models.ManyToManyField(Tag, blank=True, related_name='posts')
	post_content 	= models.TextField()
	post_publish 	= models.DateTimeField(default=timezone.now)
	post_created 	= models.DateTimeField(auto_now_add=True)
	post_updated 	= models.DateTimeField(auto_now=True)
	post_status 	= models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	post_thumbnail 	= models.ImageField(blank=True,null=True,upload_to='uploads/posts/%Y/%m/%d')
	post_slider 	= models.BooleanField(default=False)
	post_type 		= models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default='unfeatured')
	post_view   	= models.IntegerField(default=0, verbose_name='Times of viewed')

	
	class Meta:
		ordering = ('-post_publish',)
		verbose_name_plural = "Posts"

	def __str__(self):
		return self.post_title  
