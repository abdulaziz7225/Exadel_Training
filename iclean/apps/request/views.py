from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.request.models import Request, Request_status
from apps.request.serializers import RequestSerializer, RequestStatusSerializer

# Request_status model
class RequestStatusList(APIView):
    """
    List all request statuses, or create a new request status.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        request_status = Request_status.objects.all()
        serializer = RequestStatusSerializer(request_status, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequestStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestStatusDetail(APIView):
    """
    Retrieve, update or delete a request status instance.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return Request_status.objects.get(pk=pk)
        except Request_status.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        request_status = self.get_object(pk)
        serializer = RequestStatusSerializer(request_status)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        request_status = self.get_object(pk)
        serializer = RequestStatusSerializer(request_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        request_status = self.get_object(pk)
        request_status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# Request model
class RequestList(APIView):
    """
    List all requests, or create a new request.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestDetail(APIView):
    """
    Retrieve, update or delete a request instance.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return Request.objects.get(pk=pk)
        except Request.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        myrequest = self.get_object(pk)
        serializer = RequestSerializer(myrequest)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        myrequest = self.get_object(pk)
        serializer = RequestSerializer(myrequest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        myrequest = self.get_object(pk)
        myrequest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

