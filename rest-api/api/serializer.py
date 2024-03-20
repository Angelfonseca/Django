from rest_framework import serializers
from .models import User, Module, Sensor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','password','role']
        
class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id','Sensors','is_active','name']
        
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id','soilhumsens','humsens','temp']
        

        