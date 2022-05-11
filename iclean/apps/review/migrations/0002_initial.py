# Generated by Django 4.0.4 on 2022-05-11 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.client'),
        ),
        migrations.AddField(
            model_name='review',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.company'),
        ),
    ]
