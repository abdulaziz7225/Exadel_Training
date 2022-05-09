from django.db import models
from apps.request.models import Request
from apps.user.models import Company


# Create your models here.
class Notification(models.Model):
    name = models.CharField(max_length=255)
    type_of_notification = models.CharField(max_length=255)
    details = models.TextField()
    viewed_by_company = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
