# Generated by Django 4.0.4 on 2022-05-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_service_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
