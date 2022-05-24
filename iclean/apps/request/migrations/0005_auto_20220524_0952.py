# Generated by Django 4.0.4 on 2022-05-24 04:52

from django.db import migrations
from django.utils.text import slugify


def add_slug(apps, schema_editor):
    Request = apps.get_model('request', 'Request')
    for request in Request.objects.all():
        request.slug = slugify(request.name)
        request.save()


def remove_slug(apps, schema_editor):
    Request = apps.get_model('request', 'Request')
    for request in Request.objects.all():
        request.slug = None
        request.save()


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0004_request_slug'),
    ]

    operations = [
        migrations.RunPython(add_slug, remove_slug)
    ]
