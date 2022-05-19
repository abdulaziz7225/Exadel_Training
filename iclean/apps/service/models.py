from django.db import models
from django.core.validators import MinValueValidator

from apps.user.models import Company


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    type_of_service = models.CharField(max_length=255)
    cost_of_service = models.DecimalField(max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    def get_fields(self):

        my_list = []

        for field in self.__class__._meta.fields[1:]:
            if field.verbose_name != 'company':
                my_list.append((field.verbose_name, field.value_from_object(self)))
            else:
                my_list.append((field.verbose_name, Service.objects.get(pk=field.value_from_object(self)).company))
        
        return my_list

    class Meta:
        ordering = ['created_at']
