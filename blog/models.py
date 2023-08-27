from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    # thumbnail = models.ImageField()

    content = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default=None, unique=True, null=True)

    def __str__(self):
        return self.title
