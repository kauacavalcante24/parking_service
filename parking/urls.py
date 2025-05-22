from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ParkingRecordViewSet, ParkingSpotViewSet


router = DefaultRouter()
router.register('parking/records', ParkingRecordViewSet)
router.register('parking/spots', ParkingSpotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
