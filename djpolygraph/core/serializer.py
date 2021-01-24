from rest_framework import serializers
from .models import Production, TypePrint


class ProductionSerializer(serializers.Serializer):
    name_product = serializers.CharField()
    paper = serializers.StringRelatedField(many=True)

    class Meta:
        model = Production
        fields = [
            'name_product',
            'paper'
        ]


class TypePrintSerializer(serializers.Serializer):
    name_print = serializers.CharField()

    class Meta:
        model = TypePrint
        fields = [
            'name_print',
        ]