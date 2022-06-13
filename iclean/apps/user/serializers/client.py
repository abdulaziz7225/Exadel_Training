from rest_framework import serializers

from apps.user.models import Client


# Client model
class ReadClientSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field='id', read_only=True)
    # requests = serializers.HyperlinkedRelatedField(many=True, view_name='request-detail', read_only=True)
    # reviews = serializers.HyperlinkedRelatedField(many=True, view_name='review-detail', read_only=True)
    class Meta:
        model = Client
        fields = ['url', 'user', 'first_name', 'last_name', 'street', 'house_number', 
        'apartment', 'requests', 'reviews']


class CreateClientSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='id', read_only=True)
    class Meta:
        model = Client
        fields = ['url', 'user', 'first_name', 'last_name', 'street', 'house_number', 'apartment']
