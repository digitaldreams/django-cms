from django.contrib import admin

from .models import Category, Tag, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    fields = ['slug', 'title']
    search_fields = ['title']
    list_display = ['title']


class TagAdmin(admin.ModelAdmin):
    fields = ['name']
    search_fields = ['name']
    list_display = ['name']


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'status']
    search_fields = ['title', 'body']
    list_display = ['title', 'status', 'published_at']
    list_filter = ['status', 'published_at']
    date_hierarchy = 'published_at'
    actions = ['make_published']

    def make_published(self, request, queryset):
        rows_updated =queryset.update(status='published')
        if rows_updated == 1:
            message_bit = "1 post was"
        else:
            message_bit = "%s posts were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    make_published.short_description = 'Mark selected post as Published'



admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
