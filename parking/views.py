from rest_framework import viewsets
from .models import ParkingRecord, ParkingSpot
from .serializers import ParkingRecordSerializer, ParkingSpotSerializer
from .filters import ParkingSpotFilterClass, ParkingRecordFilterClass
from rest_framework.permissions import DjangoModelPermissions
from core.permissions import IsVehicleOwnerOrRecord
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['parking'])
class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    rql_filter_class = ParkingSpotFilterClass
    permission_classes = [DjangoModelPermissions]


@extend_schema(tags=['parking'])
class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    rql_filter_class = ParkingRecordFilterClass
    permission_classes = [DjangoModelPermissions, IsVehicleOwnerOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ParkingRecord.objects.all()
        return ParkingRecord.objects.filter(vehicle__owner__user=user)
