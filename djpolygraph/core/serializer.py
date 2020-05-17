from rest_framework import serializers
from .models import Production


class ProductionSerializer(serializers.Serializer):
    name_product = serializers.CharField()
    paper = serializers.StringRelatedField(many=True)

    class Meta:
        model = Production
        fields = [
            'name_product',
            'paper'
        ]
       