import json
import io
from django.contrib.sites import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# Create your views here.
from main.models import ProductModel, Car
from main.serializers import ProductSerializer, ProductSerializerModel, CarSerializer


class A ():
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def get_name(self):
        return self.name

# user = requests .get('https://jsonplaceholder.typicode.com/users/1')
# a1 = user.json()
# a = A(a1['name'], a1['username'], a1['email'])
# # res = json.dumps(a.__dict__)
# # stream = io.BytesIO(res)
# # dat = JSONParser().parse(stream)
# # print(dat)

@api_view(['GET', 'POST'])
def product(request):
    # confety = ProductModel.objects.all()
    # data = ProductSerializer(confety, many=True)
    # if request.method =='POST':
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()

    # return Response(data.data)
    if request.method == 'POST':
        serializer = ProductSerializerModel(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    confety = ProductModel.objects.all()
    data = ProductSerializerModel(confety, many=True)
    return Response(data.data)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def product_detail(request, pk):
    prod = get_object_or_404(ProductModel, pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializerModel(prod)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializerModel(instance=prod, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=201)

@api_view(['GET', 'POST', 'PUT'])
def product2_detail(request, pk):
    prod = get_object_or_404(Car, pk=pk)
    serializer = CarSerializer(prod)
    if request.method == 'PUT':
        serializer = ProductSerializer(instance=prod, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.data)
