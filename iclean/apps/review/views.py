from rest_framework.response import Response
from rest_framework import generics, renderers

from apps.review.models import Review
from apps.review.serializers import ReviewSerializer



class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


