from django.db import models
from customers.models import Customer


class VehicleType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nome')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículo'

    def __str__(self):
        return self.name


class VehicleBrand(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nome')

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='vehicles',
        blank=True,
        null=True,
        verbose_name='Proprietário'
    )
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles_type',
        verbose_name='Tipo de Veículo'
    )
    brand = models.ForeignKey(
        VehicleBrand,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles_brand',
        verbose_name='Marca'
    )
    license_plate = models.CharField(max_length=11, unique=True, verbose_name='Placa')
    model = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Modelo'
    )
    color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Cor'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Adicionado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.license_plate
