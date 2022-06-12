from rest_framework import serializers

from apps.review.models import Review


class ReadReviewSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field='full_name', read_only=True)
    company = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Review
        fields = ['url', 'id', 'comment', 'rating', 'created_at', 'client', 'company', 'slug']


class AdminCreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['url', 'id', 'comment', 'rating', 'client', 'company']


class ClientCreateReviewSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field='full_name', read_only=True)
    class Meta:
        model = Review
        fields = ['url', 'id', 'comment', 'rating', 'client', 'company']