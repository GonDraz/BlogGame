import logging
from django.shortcuts import render

from base.views import import_view
from .models import Post


def blog(request):
    Data = {'Posts': Post.objects.all().order_by("-date")}
    return render(request, import_view(view='blog'), Data)


def post(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, import_view(view='post'), {'post': post})
