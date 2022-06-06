from django.db import models

from apps.request.models import Request
from apps.user.models import Company


# Create your models here.
class Notification(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    viewed_by_company = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='notifications')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='notifications')
    slug = models.SlugField(null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.name}"
