from django.contrib import admin
from .models import Category, Newsletter, Post, Comment


class PostAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'slug',
                    'overview', 'author', 'date']

    list_filter = ['category', 'date', 'author']

    search_fields = ['id', 'title', 'slug',
                     'overview', 'author', 'date']


admin.site.register(Post, PostAdmin)


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Newsletter)
