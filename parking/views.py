from rest_framework import viewsets
from .models import ParkingRecord, ParkingSpot
from .serializers import ParkingRecordSerializer, ParkingSpotSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from core.permissions import IsVehicleOwnerOrRecord


class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions, IsVehicleOwnerOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ParkingRecord.objects.all()
        return ParkingRecord.objects.filter(vehicle__owner__user=user)


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions]
