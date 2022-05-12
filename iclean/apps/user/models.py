from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


# Create your models here.
class Role(models.Model):
    ADMIN = 1
    CLIENT = 2
    COMPANY = 3
    ROLE_CHOICES = [
        (ADMIN, 'admin'),
        (CLIENT, 'client'),
        (COMPANY, 'company'),
    ]

    id = models.PositiveSmallIntegerField(
        primary_key=True, choices=ROLE_CHOICES)

    def __str__(self):
        return self.get_id_display()


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True)
    phone = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def str(self):
        return self.email

    def get_fields(self):
        my_list = []

        for field in self.__class__._meta.fields[1:]:
            if field.verbose_name != 'role':
                my_list.append(
                    (field.verbose_name, field.value_from_object(self)))
            else:
                my_list.append((field.verbose_name, User.objects.get(
                    pk=field.value_from_object(self)).role))

        return my_list


class Client(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE, related_name='client')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.PositiveSmallIntegerField()
    apartment = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Company(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

