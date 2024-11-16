from django.shortcuts import render

from django.http import JsonResponse


from .products import products

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def getroutes(request):
    routes=[
        '/api/products',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',

    ]
    return Response(routes)

@api_view(['GET'])
def getproducts(request):
    products=Product.objects.all()
    seralizer=ProductSerializer(products,many=True)
    return Response(seralizer.data)

# @api_view(['GET'])

# def getproduct(request,pk):
#     product=None
#     for i in products:
#         if i['id']==pk:
#             product=i
#             break
#     if product:
#         return Response(product)
#     else:
#         return Response({'error':'Product not found'},status=404)

@api_view(['GET'])
def getproduct(request, pk):
    products=Product.objects.get(id=pk)
    seralizer=ProductSerializer(products,many=False)
    return Response(seralizer.data)