from rest_framework import generics
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response

from apps.service.permissions import IsStaff, IsClient, IsCompany 
from apps.service.models import Service
from apps.service.serializers import ServiceSerializer


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsStaff | IsClient | IsCompany]


    def get_queryset(self):
        if getattr(self.request.user, "company", None):
            company = self.request.user.company
            return Service.objects.filter(company=company.user.id).all()
        return Service.objects.all()


    def create(self, request):
        is_staff = getattr(self.request.user, "is_staff", None)
        is_company = getattr(self.request.user, "companys", None)
        if is_staff or is_company:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            if is_company and not (serializer.validated_data["company"].user == self.request.user):
                return Response({"message": "You don't have permission to create service with another company"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"message": "You don't have permission to create service"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsStaff | IsClient | IsCompany]


    def update(self, request, *args, **kwargs):
        is_company = getattr(self.request.user, "companys", None)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()    
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if is_company and not (serializer.validated_data["company"].user == self.request.user):
            return Response({"message": "You don't have permission to update the company of the service"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Service has been deleted"}, status=status.HTTP_204_NO_CONTENT)
