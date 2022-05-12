from django.db import models
from apps.request.models import Request
from apps.user.models import Company


# Create your models here.
class Notification(models.Model):
    name = models.CharField(max_length=100)
    type_of_notification = models.CharField(max_length=255)
    details = models.TextField()
    viewed_by_company = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    def get_fields(self):

        my_list = []

        for field in self.__class__._meta.fields[1:]:
            if field.verbose_name != 'request':
                my_list.append((field.verbose_name, field.value_from_object(self)))
            else:
                my_list.append((field.verbose_name, Notification.objects.get(pk=field.value_from_object(self)).name))
        
        return my_list