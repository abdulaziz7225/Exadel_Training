from rest_framework import generics
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response


from apps.request.models import Request, RequestStatus
from apps.request.serializers import RequestSerializer, RequestStatusSerializer


"""
RequestStatus model
"""
class RequestStatusList(generics.ListCreateAPIView):
    queryset = RequestStatus.objects.all()
    serializer_class = RequestStatusSerializer

    def create(self, request):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"message": "You don't have permission to create request status"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class RequestStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestStatus.objects.all()
    serializer_class = RequestStatusSerializer

    def update(self, request, *args, **kwargs):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response({"message": "You don't have permission to update request status"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def destroy(self, request, *args, **kwargs):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Request status has been deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "You don't have permission to delete request status"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


"""
Request model
"""
class RequestList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def get_queryset(self):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            return Request.objects.all()
        return Request.objects.filter(Q(client=self.request.user.id) | Q(company=self.request.user.id)).all()


    def create(self, request):
        is_staff = getattr(self.request.user, "is_staff", None)
        is_client = getattr(self.request.user, "clients", None)
        if is_staff or is_client: 
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            if not (is_staff or serializer.validated_data["client"].user == self.request.user):
                return Response({"message": "You don't have permission to create request with another client"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"message": "You don't have permission to create request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    
    def update(self, request, *args, **kwargs):
        is_staff = getattr(self.request.user, "is_staff", None)
        is_client = getattr(self.request.user, "clients", None)
        is_company = getattr(self.request.user, "companys", None)
        if is_staff or is_client or is_company:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            if is_client and not (serializer.validated_data["client"] == self.request.user):
                return Response({"message": "You don't have permission to update another client's request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            if is_company and not (serializer.validated_data["company"].user == self.request.user):
                return Response({"message": "You don't have permission to update another company's of request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response({"message": "You don't have permission to update request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def destroy(self, request, *args, **kwargs):
        is_staff = getattr(self.request.user, "is_staff", None)
        is_client = getattr(self.request.user, "clients", None)
        if is_staff or is_client:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Request has been deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "You don't have permission to delete request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
