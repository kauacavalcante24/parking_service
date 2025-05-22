from rest_framework import serializers
from .models import Vehicle, VehicleBrand, VehicleType


class VehicleBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleBrand
        fields = '__all__'


class VehicleTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleType
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'
