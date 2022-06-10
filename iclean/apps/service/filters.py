from django_filters.rest_framework import FilterSet

from apps.service.models import Service


class ServiceFilter(FilterSet):
    class Meta:
        model = Service
        fields = {
            'name': ['icontains'],
            'type_of_service': ['icontains'],
            'company': ['exact'],
            'cost_of_service': ['gte', 'lte'],
        }