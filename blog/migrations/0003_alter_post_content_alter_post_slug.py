# Generated by Django 4.2.4 on 2023-08-29 09:38

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_body_post_content_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=None, null=True, unique=True),
        ),
    ]
