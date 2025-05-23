from rest_framework import viewsets
from .serializers import VehicleSerializer, VehicleBrandSerializer, VehicleTypeSerializer
from .models import Vehicle, VehicleBrand, VehicleType
from .filters import VehicleBrandFilterClass, VehicleTypeFilterClass, VehicleFilterClass
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from core.permissions import IsVehicleOwnerOrRecord
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['vehicles'])
class VehicleBrandViewSet(viewsets.ModelViewSet):
    queryset = VehicleBrand.objects.all()
    serializer_class = VehicleBrandSerializer
    rql_filter_class = VehicleBrandFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]


@extend_schema(tags=['vehicles'])
class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    rql_filter_class = VehicleTypeFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]


@extend_schema(tags=['vehicles'])
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    rql_filter_class = VehicleFilterClass
    permission_classes = [DjangoModelPermissions, IsVehicleOwnerOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)
