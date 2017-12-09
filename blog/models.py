from django.db import models
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS


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
    # Meta is a special Class which used to decorate model.
    #  Model specific features e.g. ordering, db_table, indexes,permissions, get_latest_by, abstract are defined here as
    # Attribute. We can not define this as Model attribute.
    class Meta:
        ordering = ['-published_at']

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
    # limit_choices_to keyword are also used here. Which is a filter for a relationship
    # to_field keyword are used to specify foreign_key name. By default Django will use PK

    post = models.ForeignKey(Post, related_name='comments')
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """ This method will validate data before save """
        if len(self.body) < 1:
            raise ValidationError({'body': 'Body is required'})
