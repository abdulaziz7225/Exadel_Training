from rest_framework import viewsets

from apps.notification.models import Notification
from apps.notification.serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


