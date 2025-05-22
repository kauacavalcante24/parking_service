from rest_framework.permissions import BasePermission


class IsVehicleOwnerOrRecord(BasePermission):

    def has_object_permission(self, request, view, obj):

        if hasattr(obj, 'owner'):
            return obj.owner and obj.owner.user == request.user
        
        if hasattr(obj, 'vehicle') and hasattr(obj.vehicle, 'owner'):
            return obj.vehicle.owner and obj.vehicle.owner.user == request.user
        
        return False
