from rest_framework import generics

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from apps.request.permissions import AuthorAllStaffAllButEditOrReadOnly

from apps.request.models import Request, RequestStatus
from apps.request.serializers import RequestSerializer, RequestStatusSerializer

# RequestStatus model
class RequestStatusList(generics.ListCreateAPIView):
    queryset = RequestStatus.objects.all()
    serializer_class = RequestStatusSerializer

class RequestStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestStatus.objects.all()
    serializer_class = RequestStatusSerializer


# Request model
class RequestList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
