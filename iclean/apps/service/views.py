from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q

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

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def get_queryset(self):
        # return Service.objects.select_related('company').filter(company=self.request.user.id)
        # request = None
        # if self.request.user.id:
        #     request = User.objects.filter(
        #         client=self.request.user.role).first()
        # return Service.objects.filter(Q(request=getattr(request, "id", 0)) | Q(company=self.request.user.id)).all()

    # def perform_create(self, serializer):
    #     serializer.save(company=self.request.user.id)