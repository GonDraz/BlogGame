from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField(default="<p>Hello World</p>")
    date = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title
