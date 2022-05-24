# Generated by Django 4.0.4 on 2022-05-24 04:47

from django.db import migrations
from django.utils.text import slugify


def add_slug(apps, schema_editor):
    Service = apps.get_model('service', 'Service')
    for service in Service.objects.all():
        service.slug = slugify(service.name)
        service.save()

def remove_slug(apps, schema_editor):
    Service = apps.get_model('service', 'Service')
    for service in Service.objects.all():
        service.slug = None
        service.save()

class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_service_slug'),
    ]

    operations = [
        migrations.RunPython(add_slug, remove_slug)
    ]
