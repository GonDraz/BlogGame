from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):

    list_display = ['id', 'user']
    list_filter = ['user']
    search_fields = ['id', 'user']


admin.site.register(Author, AuthorAdmin)
