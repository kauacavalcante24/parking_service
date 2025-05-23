from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from .filters import CustomerFilterClass
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['customers'])
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    rql_filter_class = CustomerFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]
