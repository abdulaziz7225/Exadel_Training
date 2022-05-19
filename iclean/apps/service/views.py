from rest_framework.response import Response
from rest_framework import generics, renderers

from apps.service.models import Service
from apps.service.serializers import ServiceSerializer


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
