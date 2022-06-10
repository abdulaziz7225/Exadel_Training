from django_filters.rest_framework import FilterSet

from apps.review.models import Review


class ReviewFilter(FilterSet):
    class Meta:
        model = Review
        fields = {
            'comment': ['icontains'],
            'rating': ['gte', 'lte'],
            'client': ['exact'],
            'company': ['exact'],
        }
