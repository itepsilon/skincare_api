from django.shortcuts import render
from skincare_app.models import Product
from skincare_app.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def product_collection(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
