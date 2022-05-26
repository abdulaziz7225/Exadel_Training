from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response

from apps.service.permissions import IsStaff, IsOwner
from apps.service.models import Service
from apps.service.serializers import ServiceSerializer


class ServiceList(generics.ListCreateAPIView):
    # permission_classes = [IsStaff | IsOwner]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    # def list(self, request, *args, **kwargs):
    #     if getattr(self.request.user, "company", None):
    #         company = self.request.user.company
    #         queryset = self.filter_queryset(self.get_queryset())

    #         page = self.paginate_queryset(queryset)
    #         if page is not None:
    #             serializer = self.get_serializer(page, many=True)
    #             return self.get_paginated_response(serializer.data)

    #         serializer = self.get_serializer(queryset, many=True)
    #         return Response(serializer.data).filter(company=company.user.id)
    #         # return Service.objects.filter(company=company.user.id).all()
    #     return Service.objects.all()


    def get_queryset(self):
        if getattr(self.request.user, "company", None):
            company = self.request.user.company
            return Service.objects.filter(company=company.user.id).all()
        return Service.objects.all()


    def create(self, request):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff or getattr(self.request.user, "company", None):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            if not (is_staff or serializer.validated_data["company"].name == self.request.user.company.name):
                return Response({"message": "You don't have permission to create service"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"message": "You don't have permission to create service"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def perform_create(self, serializer):
        serializer.save(company=self.request.user)


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):

    # permission_classes = [IsStaff | IsOwner]
    # print(IsOwnerOrReadOnly)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    def get_queryset(self):
        if getattr(self.request.user, "company", None):
            company = self.request.user.company
            return Service.objects.filter(company=company.user.id).all()
        return Service.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     is_staff = getattr(self.request.user, "is_staff", None)
    #     if is_staff or getattr(self.request.user, "company", None):
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance)
    #         return Response(serializer.data)
    #     return Response({"message": "You don't have permission to retrieve service"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def update(self, request, *args, **kwargs):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff or getattr(self.request.user, "company", None):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            if not (is_staff or serializer.validated_data["company"].name == self.request.user.company.name):
                return Response({"message": "You don't have permission to update the company of service"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response({"message": "You don't have permission to update service"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def destroy(self, request, *args, **kwargs):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff or getattr(self.request.user, "company", None):
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Item has been deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "You don't have permission to delete service"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)