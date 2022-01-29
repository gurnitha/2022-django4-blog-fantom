# 2022-django4-blog-fantom
This is my exercise based on MyLearning on Udemy made by Mr. Volkan Altis and Webformyself

Github repository: https://github.com/gurnitha/2022-django4-blog-fantom



### 1. SETTING UP A FULLY STATIC FONTOM BLOG
--------------------------------------------

#### 1.1 Created django project, apps, pages and added static, media files and themes

        NOTE: Bellow is the project's structure

        E:.
        ├───apps
        │   ├───blog
        │   │   ├───migrations
        │   │   │   └───__pycache__
        │   │   ├───templates
        │   │   │   └───blog
        │   │   │       ├───inc
        │   │   │       └───shared
        │   │   └───__pycache__
        │   ├───contactus
        │   │   ├───migrations
        │   │   │   └───__pycache__
        │   │   ├───templates
        │   │   │   └───contactus
        │   │   └───__pycache__
        │   └───users
        │       ├───migrations
        │       │   └───__pycache__
        │       ├───templates
        │       │   └───users
        │       └───__pycache__
        ├───config
        │   ├───static
        │   └───__pycache__
        └───templates
            └───shared

        modified:   README.md


### 2. DJANGO MODELS
--------------------

#### 2.1 Created models: Category, Tag, Post and Profile and added some post_slider items

        modified:   README.md
        modified:   apps/blog/admin.py
        new file:   apps/blog/migrations/0001_initial.py
        new file:   apps/blog/migrations/0002_initial.py
        modified:   apps/blog/models.py
        modified:   apps/users/admin.py
        new file:   apps/users/migrations/0001_initial.py
        modified:   apps/users/models.py
        new file:   media/profiles/ing-sm.jpg
        new file:   media/profiles/user-img.jpg
        new file:   media/uploads/posts/2022/01/28/post-cat-1.jpg
        new file:   media/uploads/posts/2022/01/28/post-cat-2.jpg
        new file:   media/uploads/posts/2022/01/28/post-s-1.jpg
        new file:   media/uploads/posts/2022/01/28/post-s-2.jpg
        new file:   media/uploads/posts/2022/01/28/post-s-3.jpg
        new file:   media/uploads/posts/2022/01/28/post-s-4.jpg

        NOTE: :)


### 3. FULLY DYNAMIC HOME PAGE
------------------------------

#### 3.1 Loading and fetching post_sliders from db

        modified:   README.md
        modified:   apps/blog/templates/blog/inc/slider.html
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py


        NOTE: :)

        Pay attention to fetch items which have ManyToMany relationship.


#### 3.2 Loading and fetching featured and small posts fro db to homepage

        modified:   README.md
        new file:   apps/blog/migrations/0003_alter_post_post_slug_alter_post_post_type.py
        new file:   apps/blog/migrations/0004_alter_post_post_type.py
        modified:   apps/blog/models.py
        modified:   apps/blog/templates/blog/inc/content_main.html
        modified:   apps/blog/views.py
        new file:   media/uploads/posts/2022/01/28/blog-1.jpg
        ...
        new file:   media/uploads/posts/2022/01/28/blog-small-3.jpg


        NOTE: 

        1. Modified Post model: adding post_type 'small'

        :)


#### 3.3 Pagination using GCBV

        modified:   README.md
        modified:   apps/blog/templates/blog/inc/content_main.html
        modified:   apps/blog/templates/blog/shared/pagination.html
        modified:   apps/blog/views.py


        NOTE: 

        1. Could not loop small post_type as extra query.
        2. Only featured post_type could be loope as it should be

        :) and :(


#### 3.4 POPULAR POSTS - Load and fetch popular posts

        STEPS:

        1. Create templatetags folder   : apps/blog/templatetags
        2. Create init file             : apps/blog/templatetags/__init__.py
        3. Create templatetags file     : apps/blog/templatetags/template_tags_blog.py
        4. In template_tags_blog.py     : Define show_popular_posts view method and its logic
                                          to create objects of post_type='featured'
        5. In templates/blog/index.html : Load {% load template_tags_blog %}  
                                          and fetch the show_popular_posts view method
        6. Test it out 

        modified:   README.md
        modified:   apps/blog/templates/blog/index.html
        modified:   apps/blog/templates/blog/shared/aside_popular_posts.html
        new file:   apps/blog/templatetags/__init__.py
        new file:   apps/blog/templatetags/template_tags_blog.py

        NOTE: :)


#### 3.5 POSTS BY CATEGORY - Showing categories and number of posts in each category

        STEPS:

        1. Follow steps in 3.4
        2. In Category model, create post_count method by using 
           the related_name='posts' in Post model
           def post_count(self):
               return self.posts.all().count()
        3. Load templatetags 
        4. Fetch the show_posts_by_category
        5. Test it out

        modified:   README.md
        modified:   apps/blog/models.py
        modified:   apps/blog/templates/blog/index.html
        modified:   apps/blog/templates/blog/shared/aside_category.html
        modified:   apps/blog/templatetags/template_tags_blog.py

        NOTE: :)


#### 3.6 POSTS BY TAG - Showing tags and number of posts in each tag

        STEPS:

        1. Refer to poin 3.5

        modified:   README.md
        modified:   apps/blog/models.py
        modified:   apps/blog/templates/blog/index.html
        modified:   apps/blog/templates/blog/shared/aside_tags.html
        modified:   apps/blog/templatetags/template_tags_blog.py

        NOTE: :)