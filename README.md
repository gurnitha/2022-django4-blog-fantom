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