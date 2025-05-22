from rest_framework import viewsets
from .serializers import VehicleSerializer, VehicleBrandSerializer, VehicleTypeSerializer
from .models import Vehicle, VehicleBrand, VehicleType
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser


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
    permission_classes = [DjangoModelPermissions]
