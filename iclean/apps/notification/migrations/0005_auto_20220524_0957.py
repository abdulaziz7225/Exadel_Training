# Generated by Django 4.0.4 on 2022-05-24 04:57

# Generated by Django 4.0.4 on 2022-05-24 04:52
from django.db import migrations
from django.utils.text import slugify


def add_slug(apps, schema_editor):
    Notification = apps.get_model('notification', 'Notification')
    for notification in Notification.objects.all():
        notification.slug = slugify(notification.name)
        notification.save()


def remove_slug(apps, schema_editor):
    Notification = apps.get_model('notification', 'Notification')
    for notification in Notification.objects.all():
        notification.slug = None
        notification.save()


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_notification_slug'),
    ]

    operations = [
        migrations.RunPython(add_slug, remove_slug)
    ]
