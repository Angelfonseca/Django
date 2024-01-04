from rest_framework import viewsets
from .serializer import UserSerializer, ProductSerializer, BarcodeSerializer
from .models import Product, User, Barcode
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BarcodeViewSet(viewsets.ModelViewSet):
    queryset = Barcode.objects.all()
    serializer_class = BarcodeSerializer
    
@csrf_exempt
def scan_barcode(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        barcode_value = data.get('barcode', '')

        # Guarda el código de barras en la base de datos
        barcode = Barcode.objects.create(code=barcode_value)
        barcode.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})