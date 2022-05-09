from django.db import models
from apps.user.models import Client, Company
from apps.service.models import Service


# Create your models here.
class Request_status(models.Model):
    name = models.CharField(max_length=255)


class Request(models.Model):
    name = models.CharField(max_length=255)
    type_of_request = models.CharField(max_length=255)
    total_area = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Request_status, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
