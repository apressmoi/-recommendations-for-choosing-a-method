from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Production, Profile
from .serializer import ProductionSerializer, TypePrintSerializer


class RenderChoicesPaper(APIView):
    lookup_field = 'name_product'

    def get(self, request, name_product, *args, **kwargs):
        production = Production.objects.filter(name_product=name_product)
        serializer = ProductionSerializer(production, many=True)
        return Response(serializer.data)


class ChoiceResult(APIView):
    lookup_field = 'username'

    def get(self, request, username, *args, **kwargs):
        result = Profile.objects.get(user__username=username).result
        serializer = TypePrintSerializer(result)
        return Response(serializer.data)
