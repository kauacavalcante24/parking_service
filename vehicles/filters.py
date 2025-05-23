from dj_rql.filter_cls import AutoRQLFilterClass
from .models import VehicleBrand, VehicleType, Vehicle


class VehicleBrandFilterClass(AutoRQLFilterClass):
    MODEL = VehicleBrand


class VehicleTypeFilterClass(AutoRQLFilterClass):
    MODEL = VehicleType


class VehicleFilterClass(AutoRQLFilterClass):
    MODEL = Vehicle
    FILTERS = (
        {
            'filter': 'user',
            'source': 'owner__name',
        },
    )
