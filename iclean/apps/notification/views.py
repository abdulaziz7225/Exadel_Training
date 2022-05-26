from rest_framework import generics
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response


from apps.notification.models import Notification
from apps.notification.serializers import NotificationSerializer
from apps.request.models import Request

class NotificationList(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            return Notification.objects.all()
        request = None    
        if self.request.user.id:
            request = Request.objects.filter(
                client=self.request.user.id).first()
        return Notification.objects.filter(Q(request=getattr(request, "id", 0)) | Q(company=self.request.user.id)).all()


    def create(self, request):
        is_staff = getattr(self.request.user, "is_staff", None)
        is_client = getattr(self.request.user, "clients", None)
        is_company = getattr(self.request.user, "companys", None)
        if is_staff or is_client or is_company:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            if is_company and not (serializer.validated_data["company"].user == self.request.user):
                return Response({"message": "You don't have permission to create notification with another company name"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"message": "You don't have permission to create notification"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


    def update(self, request, *args, **kwargs):
        is_staff = getattr(self.request.user, "is_staff", None)
        is_client = getattr(self.request.user, "clients", None)
        is_company = getattr(self.request.user, "companys", None)
        if is_staff or is_client or is_company:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            # print(serializer.validated_data)
            if is_company and not (serializer.validated_data["company"].user == self.request.user):
                return Response({"message": "You don't have permission to update the company of notification"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response({"message": "You don't have permission to update notification"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def destroy(self, request, *args, **kwargs):
        is_staff = getattr(self.request.user, "is_staff", None)
        is_client = getattr(self.request.user, "clients", None)
        if is_staff or is_client:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Notification has been deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "You don't have permission to delete notification"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)