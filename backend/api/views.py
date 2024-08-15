from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import*


# Create your views here.

class FileCL(generics.ListCreateAPIView):
 queryset=File.objects.all()
 serializer_class=FileSerializer
 
class FileRUD(generics.RetriveUpdateDestroyView):
 queryset=File.objects.all()
 serializer_class=FileSerializer
 
 
     