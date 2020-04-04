from django.shortcuts import render
from skincare_app.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response

class ListProducts(APIView):
    """
    View to list all products.
    """

    def get(self, request):
        """
        Return a list of all products.
        """
        products = Product.objects.all()
        return Response(products)
