from django.db import models


class Profile(models.Model):
    avatar = models.ImageField()
    bio = models.CharField(max_length=100, null=False)
    slug = models.SlugField(default=None, unique=True, null=True)

    def __str__(self):
        return


class Account(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    profile = Profile()

    date_sign_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return

    def full_name():
        return  # first_name.value + last_name
