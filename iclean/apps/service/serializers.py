from rest_framework import serializers

from apps.service.models import Service
from apps.user.models import Company


class ServiceSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(slug_field='name', queryset=Company.objects.all())
    class Meta:
        model = Service
        fields = ['id', 'name', 'type_of_service', 'cost_of_service', 'created_at', 'company']