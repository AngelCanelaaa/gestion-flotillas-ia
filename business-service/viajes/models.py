from django.db import models
from vehiculos.models import Vehiculo
from choferes.models import Chofer


class Viaje(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        EN_CURSO = 'en_curso', 'En curso'
        FINALIZADO = 'finalizado', 'Finalizado'
        CANCELADO = 'cancelado', 'Cancelado'

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT, related_name='viajes')
    chofer = models.ForeignKey(Chofer, on_delete=models.PROTECT, related_name='viajes')
    # FK Lógica hacia Ruta (se creará en el Sprint 2)
    ruta_id = models.PositiveIntegerField(help_text='ID de la ruta asignada')
    
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'
        ordering = ['-creado_en']

    def __str__(self):
        return f'Viaje {self.id} - {self.chofer.nombre} en {self.vehiculo.placa}'