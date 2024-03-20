from rest_framework import viewsets
from .serializer import UserSerializer, ModuloSerializer, SensorSerializer
from .models import Module, User, Sensor
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuloSerializer
    
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

