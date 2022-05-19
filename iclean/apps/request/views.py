from rest_framework.response import Response
from rest_framework import renderers, generics

from apps.request.models import Request, Request_status
from apps.request.serializers import RequestSerializer, RequestStatusSerializer


# Request_status model
class RequestStatusList(generics.ListCreateAPIView):
    queryset = Request_status.objects.all()
    serializer_class = RequestStatusSerializer


class RequestStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request_status.objects.all()
    serializer_class = RequestStatusSerializer


# Request model
class RequestList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
