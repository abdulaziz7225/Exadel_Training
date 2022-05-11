from django.db import models
from apps.user.models import Client, Company

# Create your models here.
class Review(models.Model):
    comment = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)