from django.db import models

class Ruta(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    distancia_km = models.FloatField(help_text='Distancia en kilómetros')

    class Meta:
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'
        ordering = ['origen']

    def __str__(self):
        return f'{self.origen} -> {self.destino} ({self.distancia_km} km)'