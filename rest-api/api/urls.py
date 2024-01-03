from django.urls import path,include
from rest_framework import routers
from api import views
from django.urls import path
from .views import read_barcode


router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'products',views.ProductViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('read-barcode/', read_barcode, name='read_barcode'),
]