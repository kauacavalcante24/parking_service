from rest_framework import viewsets
from .serializers import VehicleSerializer, VehicleBrandSerializer, VehicleTypeSerializer
from .models import Vehicle, VehicleBrand, VehicleType
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from core.permissions import IsVehicleOwnerOrRecord


class VehicleBrandViewSet(viewsets.ModelViewSet):
    queryset = VehicleBrand.objects.all()
    serializer_class = VehicleBrandSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [DjangoModelPermissions, IsVehicleOwnerOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)
