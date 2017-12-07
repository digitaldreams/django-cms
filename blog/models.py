from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=250, unique=True)
    title = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    statuses = (
        ('published', 'Published'),
        ('pending', 'Pending'),
        ('canceled', 'Canceled')
    )
    title = models.CharField(max_length=250, blank=True)
    body = models.TextField(blank=True)
    status = models.CharField(max_length=100, choices=statuses)
    published_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Like(models.Model):
    posts = models.ManyToManyField(Post)
    ip = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.IntegerField(default=None)
    # here we assign related_name=comments so that we can able to access this relation
    # from Post class as Post.comments not Post.comment_set
    post = models.ForeignKey(Post, related_name='comments')
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
