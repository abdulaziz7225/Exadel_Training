from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.service.models import Service
from apps.service.serializers import ServiceSerializer



class ServiceList(APIView):
    """
    List all services, or create a new service.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceDetail(APIView):
    """
    Retrieve, update or delete a service instance.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        service = self.get_object(pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

