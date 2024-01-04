from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'barcodes', views.BarcodeViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Rutas generadas por el router
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('scan-barcode/', views.scan_barcode, name='scan_barcode'),  # Nueva ruta para escanear códigos de barras
]
