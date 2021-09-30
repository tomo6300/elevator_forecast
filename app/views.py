from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Floor
from .serializer import FloorSerializer

def index(req):
  return HttpResponse('Hello World')

class FloorViewSet(viewsets.ModelViewSet):
  queryset = Floor.objects.all()
  serializer_class = FloorSerializer