from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.service.models import Service
from apps.service.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

