from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'modules', views.ModuleViewSet)
router.register(r'sensors', views.SensorViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Rutas generadas por el router
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
