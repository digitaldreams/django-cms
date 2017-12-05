from django.db import models


class Category(models.Model):
    slug = models.CharField(max_length=250, unique=True)
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
    title = models.CharField(250, blank=True),
    body = models.TextField(blank=True),
    published_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=statuses)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Like(models.Model):
    posts = models.ManyToManyField(Post)
    ip = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
