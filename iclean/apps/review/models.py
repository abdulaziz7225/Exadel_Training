from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.user.models import Client, Company


# Create your models here.
class Review(models.Model):
    comment = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.client} - ({self.created_at})"

    def get_fields(self):
        
        my_list = []

        for field in self.__class__._meta.fields[1:]:
            if field.verbose_name != 'client':
                my_list.append((field.verbose_name, field.value_from_object(self)))
            else:
                my_list.append((field.verbose_name, Review.objects.get(pk=field.value_from_object(self)).client))
        
        return my_list


