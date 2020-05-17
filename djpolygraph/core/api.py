from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Production
from .serializer import ProductionSerializer


class RenderChoicesPaper(APIView):
    lookup_field = 'name_product'

    def get(self, request, name_product, *args, **kwargs):
        production = Production.objects.filter(name_product=name_product)
        serializer = ProductionSerializer(production, many=True)
        print(serializer.data)
        return Response(serializer.data)