from django.db import models
from apps.user.models import Company

# Create your models here.


class Service(models.Model):
    company = models.CharField(max_length=255)
    type_of_service = models.CharField(max_length=255)
    cost_of_service = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
