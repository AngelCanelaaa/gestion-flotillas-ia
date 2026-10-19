from django.db import models


class Vehiculo(models.Model):
    class Estado(models.TextChoices):
        DISPONIBLE = 'disponible', 'Disponible'
        EN_VIAJE = 'en_viaje', 'En viaje'
        EN_MANTENIMIENTO = 'en_mantenimiento', 'En mantenimiento'
        FUERA_DE_SERVICIO = 'fuera_de_servicio', 'Fuera de servicio'

    numero_serie = models.CharField(
        max_length=17,
        unique=True,
        help_text='VIN de 17 caracteres. Inmutable tras la creación.',
    )
    placa = models.CharField(max_length=15)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField(help_text='Capacidad en kg')
    odometro_km = models.FloatField(default=0.0) # <-- Corregido a float según el ER
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.DISPONIBLE,
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
        ordering = ['-creado_en']

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.placa})'

    def save(self, *args, **kwargs):
        if self.pk:
            original = (
                Vehiculo.objects.filter(pk=self.pk)
                .values_list('numero_serie', flat=True)
                .first()
            )
            if original and original != self.numero_serie:
                raise ValueError(
                    'El número de serie (VIN) es inmutable y no puede modificarse.'
                )
        super().save(*args, **kwargs)