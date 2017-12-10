from django.db import models
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


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
    slug = models.SlugField(max_length=250, unique=True, null=True)
    body = models.TextField(blank=True)
    status = models.CharField(max_length=100, choices=statuses)
    published_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:posts.show', args=[str(self.slug)])


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

    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """ This method will validate data before save """
        if len(self.body) < 1:
            raise ValidationError({'body': 'Body is required'})


@receiver(pre_save, sender=Post)
def makeSlug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
    total = Post.objects.filter(slug=slugify(instance.title)).count()
    if total:
        real_total = Post.objects.filter(slug__startswith=slugify(instance.title)).count()
        instance.slug = instance.slug + "-" + str(real_total)
