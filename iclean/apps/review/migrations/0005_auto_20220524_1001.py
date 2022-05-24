# Generated by Django 4.0.4 on 2022-05-24 05:01

from django.db import migrations
from django.utils.text import slugify


def add_slug(apps, schema_editor):
    Review = apps.get_model('review', 'Review')
    for review in Review.objects.all():
        review.slug = slugify(review.comment)
        review.save()


def remove_slug(apps, schema_editor):
    Review = apps.get_model('review', 'Review')
    for review in Review.objects.all():
        review.slug = None
        review.save()


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_review_slug'),
    ]

    operations = [
        migrations.RunPython(add_slug, remove_slug)
    ]
