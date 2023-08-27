import logging
from django.shortcuts import render
from .models import Post


def blog(request):
    Data = {'Posts': Post.objects.all().order_by("-date")}
    return render(request, 'html/pages/blog.html', Data)


def post(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'html/pages/post.html', {'post': post})
