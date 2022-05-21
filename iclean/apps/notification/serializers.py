from rest_framework import serializers

from apps.notification.models import Notification
from apps.request.models import Request
from apps.user.models import Company


class NotificationSerializer(serializers.ModelSerializer):
    request = serializers.SlugRelatedField(slug_field='name', queryset=Request.objects.all())
    company = serializers.SlugRelatedField(slug_field='name', queryset=Company.objects.all())
    class Meta:
        model = Notification
        fields = ['id', 'name', 'details', 'viewed_by_company',
                  'created_at', 'request', 'company']
