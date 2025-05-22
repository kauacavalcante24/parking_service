from django.contrib import admin
from .models import Vehicle, VehicleBrand, VehicleType


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(VehicleBrand)
class VehicleBrand(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name']


@admin.register(Vehicle)
class Vehicle(admin.ModelAdmin):
    list_display = ['license_plate', 'brand', 'model', 'color', 'created_at', 'updated_at']
    search_fields = ['license_plate', 'brand', 'model']
    list_filter = ['vehicle_type']
