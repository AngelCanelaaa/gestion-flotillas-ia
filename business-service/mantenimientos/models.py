from django.db import models
from vehiculos.models import Vehiculo

class Mantenimiento(models.Model):
    class Estado(models.TextChoices):
        ABIERTO = 'abierto', 'Abierto'
        CERRADO = 'cerrado', 'Cerrado'

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT, related_name='mantenimientos')
    tipo = models.CharField(max_length=50)
    fecha = models.DateField()
    km_al_momento = models.FloatField()
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.ABIERTO)
    notas = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'
        ordering = ['-fecha']

    def __str__(self):
        return f'{self.vehiculo.placa} - {self.tipo} ({self.estado})'