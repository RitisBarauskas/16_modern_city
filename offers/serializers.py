from rest_framework.serializers import ModelSerializer

from offers.models import Review


class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
