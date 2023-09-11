import logging
from django.shortcuts import render

from base.views import import_view
from .models import Category, Post


def blog(request):
    Categorys = Category.objects.all()
    Ports = Post.objects.all().order_by("-date")

    context = {"Categorys": Categorys, "Posts": Ports}

    return render(request, import_view(view='blog'), context)


def post(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, import_view(view='post'), {'post': post})
