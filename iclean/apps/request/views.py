from rest_framework import viewsets

from apps.request.models import Request, Request_status
from apps.request.serializers import RequestSerializer, RequestStatusSerializer


# Request_status model
class RequestStatusViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Request_status.objects.all()
    serializer_class = RequestStatusSerializer


# Request model
class RequestViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


