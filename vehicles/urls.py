from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleBrandViewSet, VehicleTypeViewSet, VehicleViewSet


router = DefaultRouter()
router.register('vehicles/brands', VehicleBrandViewSet)
router.register('vehicles/types', VehicleTypeViewSet)
router.register('vehicles', VehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
