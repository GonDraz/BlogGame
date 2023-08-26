from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'content', 'date', 'slug']
    list_filter = ['date']
    search_fields = ['id', 'title', 'content', 'date', 'slug']


admin.site.register(Post, PostAdmin)
