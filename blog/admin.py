from django.contrib import admin
from django import forms
from .models import Category, Tag, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title','slug']
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    fields = ['name']
    search_fields = ['name']
    list_display = ['name']


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'status']
    search_fields = ['title', 'body']
    list_display = ['title', 'status', 'published_at', 'category']
    list_filter = ['status', 'published_at']
    date_hierarchy = 'published_at'
    actions = ['make_published']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='published')
        if rows_updated == 1:
            message_bit = "1 post was"
        else:
            message_bit = "%s posts were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    make_published.short_description = 'Mark selected post as Published'

    def category(self, obj):
        return 'Not implemented yet!'

    category.short_description = 'Category'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
