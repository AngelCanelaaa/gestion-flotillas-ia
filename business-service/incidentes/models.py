from django.db import models
from viajes.models import Viaje
from choferes.models import Chofer

class Incidente(models.Model):
    class Estado(models.TextChoices):
        ABIERTO = 'abierto', 'Abierto'
        EN_ATENCION = 'en_atencion', 'En atención'
        ATENDIDO = 'atendido', 'Atendido'
        DESCARTADO = 'descartado', 'Descartado'

    class Tipo(models.TextChoices):
        OJO_CERRADO = 'ojo_cerrado', 'Ojo cerrado'
        BOSTEZO = 'bostezo', 'Bostezo'

    viaje = models.ForeignKey(Viaje, on_delete=models.PROTECT, related_name='incidentes')
    chofer = models.ForeignKey(Chofer, on_delete=models.PROTECT, related_name='incidentes')
    episodio_id = models.CharField(max_length=50, unique=True, help_text='ID compartido con MongoDB')
    
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    nivel_riesgo = models.CharField(max_length=20) # Ej: 'alto', 'medio', 'critico'
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.ABIERTO)
    
    # FK Lógica a Identidad (Admin que atiende)
    admin_asignado_id = models.PositiveIntegerField(null=True, blank=True)
    
    duracion_episodio_seg = models.FloatField()
    confianza_maxima = models.FloatField()
    
    detectado_en = models.DateTimeField()
    notas_resolucion = models.TextField(null=True, blank=True)
    
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Incidente'
        verbose_name_plural = 'Incidentes'
        ordering = ['-detectado_en']

    def __str__(self):
        return f'Incidente {self.id} - {self.tipo} ({self.estado})'


class IncidenteHistorial(models.Model):
    """Log inmutable de auditoría. Solo INSERT, nunca UPDATE ni DELETE."""
    incidente = models.ForeignKey(Incidente, on_delete=models.CASCADE, related_name='historial')
    estado_anterior = models.CharField(max_length=20, null=True, blank=True)
    estado_nuevo = models.CharField(max_length=20)
    
    # FK Lógica a Identidad (quién hizo el cambio)
    cambiado_por_id = models.PositiveIntegerField()
    
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Historial de Incidente'
        verbose_name_plural = 'Historial de Incidentes'
        ordering = ['-fecha_cambio']