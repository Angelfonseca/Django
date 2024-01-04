from rest_framework import serializers
from .models import User
from .models import Product
from .models import Barcode

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','password','role','curp','is_active']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','code','stock']
        
class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = ['id','code','created_at']
        