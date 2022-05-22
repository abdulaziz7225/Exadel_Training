from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q

from apps.notification.models import Notification
from apps.notification.serializers import NotificationSerializer
from apps.request.models import Request


class NotificationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        request = None
        if self.request.user.id:
            request = Request.objects.filter(
                client=self.request.user.id).first()
        return Notification.objects.filter(Q(request=getattr(request, "id", 0)) | Q(company=self.request.user.id)).all()
