from rest_framework import viewsets
from .serializer import UserSerializer, ProductSerializer
from .models import Product, User
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['POST'])
def read_barcode(request):
    barcode_data = request.data.get('barcode_data')
    if barcode_data:
        try:
            # Hacer una solicitud a un servicio web (puedes usar tu propia instancia de ZXing o un servicio público)
            zxing_url = 'https://zxing.org/w/decode'
            response = requests.get(zxing_url, params={'u': barcode_data})
            
            # Analizar la respuesta JSON
            result = response.json()
            
            return Response(result)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
    else:
        return Response({'error': 'No se proporcionó el dato del código de barras'}, status=400)
