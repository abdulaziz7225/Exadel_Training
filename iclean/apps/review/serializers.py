from rest_framework import serializers

from apps.review.models import Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.ReadOnlyField(source='client.first_name')
    company = serializers.ReadOnlyField(source='company.name')
    class Meta:
        model = Review
        fields = ['url', 'id', 'comment', 'rating', 'created_at', 'client', 'company']
