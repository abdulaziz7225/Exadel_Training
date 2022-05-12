from django.db import models
from django.core.validators import MinValueValidator

from apps.user.models import Client, Company
from apps.service.models import Service


# Create your models here.
class Request_status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Request(models.Model):
    name = models.CharField(max_length=100)
    type_of_request = models.CharField(max_length=255)
    total_area = models.DecimalField(max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.ForeignKey(Request_status, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


    def get_fields(self):
        
        my_list = []

        for field in self.__class__._meta.fields[1:]:
            if field.verbose_name != 'status':
                my_list.append((field.verbose_name, field.value_from_object(self)))
            else:
                my_list.append((field.verbose_name, Request.objects.get(pk=field.value_from_object(self)).status))
            
        return my_list
