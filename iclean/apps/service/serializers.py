from rest_framework import serializers


from apps.service.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'type_of_service', 'cost_of_service', 'created_at', 'company']