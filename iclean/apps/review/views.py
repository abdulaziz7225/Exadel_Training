from rest_framework import viewsets

from apps.review.models import Review
from apps.review.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



