from django.db import models
from vehicles.models import Vehicle


class ParkingSpot(models.Model):
    spot_number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Número da Vaga'
    )
    is_occupied = models.BooleanField(
        default=False,
        verbose_name='Situação'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Adicionado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return self.spot_number


class ParkingRecord(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        related_name='parking_records',
        on_delete=models.PROTECT,
        verbose_name='Veículo'
    )
    parking_spot = models.ForeignKey(
        ParkingSpot,
        related_name='parking_spots',
        on_delete=models.PROTECT,
        verbose_name='Vaga'
    )
    entry_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Horário de Entrada'
    )
    exit_time = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Horário de Saída'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Adicionado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )


    class Meta:
        ordering = ['created_at']
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'


    def __str__(self):
        return f'{self.vehicle} - {self.parking_spot} - {self.entry_time}'
