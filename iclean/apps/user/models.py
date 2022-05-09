# import email
from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    role = models.CharField(max_length=255)


class User(models.Model):
    # user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    role_id = models.ForeignKey(Role, on_delete=models.PROTECT)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.IntegerField()
    apartment = models.CharField(max_length=255)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=255)


