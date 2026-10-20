from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    class Rol(models.TextChoices):
        ADMINISTRADOR = 'administrador', 'Administrador de Flotilla'
        CONDUCTOR = 'conductor', 'Conductor'

    rol = models.CharField(
        max_length=20,
        choices=Rol.choices,
        default=Rol.CONDUCTOR,
    )
    # Puedes agregar más campos aquí en el futuro (ej. teléfono, foto, etc.)

    def __str__(self):
        return f'{self.username} ({self.get_rol_display()})'