from rest_framework import generics

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from apps.review.permissions import IsOwnerOrReadOnly

from apps.review.models import Review
from apps.review.serializers import ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


