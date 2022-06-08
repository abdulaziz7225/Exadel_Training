from rest_framework import serializers

from apps.review.models import Review
from apps.user.models import Client, Company


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.SlugRelatedField(slug_field='first_name', queryset=Client.objects.all())
    company = serializers.SlugRelatedField(slug_field='name', queryset=Company.objects.all())
    class Meta:
        model = Review
        fields = ['url', 'id', 'comment', 'rating', 'created_at', 'client', 'company' 'slug']
