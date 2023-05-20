from ast import Return
from urllib import response
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import bookacallserializer , contactformserializer
from .models import Bookacall , contactform
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
# Create your views here.

@api_view(['get','POST'])
@csrf_exempt
@parser_classes([JSONParser])
def bookacallview(request):
    if request.method  == 'POST':
        serializer = bookacallserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)




@api_view(['get','POST'])
@csrf_exempt
@parser_classes([JSONParser])
def contactformview(request):
    if request.method  == 'POST':
        serializer = contactformserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)