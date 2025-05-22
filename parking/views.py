from rest_framework import viewsets
from .models import ParkingRecord, ParkingSpot
from .serializers import ParkingRecordSerializer, ParkingSpotSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser


class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions]
