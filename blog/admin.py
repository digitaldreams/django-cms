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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
