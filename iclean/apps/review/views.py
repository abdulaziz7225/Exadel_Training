from rest_framework import viewsets
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response

from apps.review.permissions import IsStaff, IsClient, IsCompany 
from apps.review.models import Review
from apps.review.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsStaff | IsClient | IsCompany]


    def get_queryset(self):
        is_staff = getattr(self.request.user, "is_staff", None)
        if is_staff:
            return Review.objects.all()
        return Review.objects.filter(Q(client=self.request.user.id) | Q(company=self.request.user.id)).all()


    def create(self, request):
        is_client = getattr(self.request.user, "clients", None)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if is_client and not (serializer.validated_data["client"].user == self.request.user):
            return Response({"message": "You don't have permission to create review for another client"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def update(self, request, *args, **kwargs):
        is_client = getattr(self.request.user, "clients", None)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if is_client and not (serializer.validated_data["client"].user == self.request.user):
            return Response({"message": "You don't have permission to update the client of the review"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Review has been deleted"}, status=status.HTTP_204_NO_CONTENT)