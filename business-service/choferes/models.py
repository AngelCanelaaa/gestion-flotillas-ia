from django.db import models


class Chofer(models.Model):
    class Estado(models.TextChoices):
        DISPONIBLE = 'disponible', 'Disponible'
        EN_VIAJE = 'en_viaje', 'En viaje'
        INACTIVO = 'inactivo', 'Inactivo'

    # FK Lógica hacia el microservicio de Identidad (sin integridad referencial física)
    usuario_id = models.PositiveIntegerField(
        unique=True,
        help_text='ID del usuario en el servicio de identidad'
    )
    nombre = models.CharField(max_length=100)
    licencia = models.CharField(max_length=20)
    licencia_vencimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    emergencia = models.CharField(
        max_length=100, 
        help_text='Nombre y teléfono de contacto de emergencia'
    )
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.DISPONIBLE,
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Chofer'
        verbose_name_plural = 'Choferes'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} - Licencia: {self.licencia}'