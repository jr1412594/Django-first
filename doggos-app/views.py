from django.shortcuts import render
from rest_framework import status, viewsets
from .models import Dog
from .serializers import DogSerializer
# Create your views here.

class DogView(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer