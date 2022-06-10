from rest_framework import serializers

from apps.notification.models import Notification
from apps.request.models import Request
from apps.user.models import Company


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    request = serializers.SlugRelatedField(
        slug_field='name', queryset=Request.objects.all())
    company = serializers.SlugRelatedField(
        slug_field='name', queryset=Company.objects.all())

    class Meta:
        model = Notification
        fields = ['url', 'id', 'name', 'details', 'viewed_by_company',
                  'created_at', 'request', 'company', 'slug']
