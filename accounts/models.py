# -*- coding: utf-8 -*-
from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image


class Author(models.Model):

    first_name = models.CharField(default= "",null=False, blank=False, max_length=100)
    last_name = models.CharField(default= "", null=False, blank=False, max_length=20)

    user = models.OneToOneField(
        User, verbose_name=_("User"), on_delete=models.CASCADE)

    # birthday = models.DateField(null=False, blank=False)

    email = models.EmailField(default="@gmail.com",
                              unique=True, null=True, blank=False)
    picture = models.ImageField(
        _("Picture"), upload_to="thumbnail", default="testing.jpeg", blank=True
    )

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.user.get_full_name()

    def full_name(self):
        return self.last_name + self.first_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.picture:  # pragma: no cover
            img = Image.open(default_storage.open(self.picture.name))
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                buffer = BytesIO()
                img.save(buffer, format="JPEG")
                default_storage.save(self.picture.name, buffer)
