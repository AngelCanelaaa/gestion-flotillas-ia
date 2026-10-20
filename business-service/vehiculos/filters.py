import django_filters
from .models import Vehiculo

class VehiculoFilter(django_filters.FilterSet):
    class Meta:
        model = Vehiculo
        fields = {
            'estado': ['exact'],
            'marca': ['icontains'],      # icontains = búsqueda parcial, sin distinguir mayúsculas
            'placa': ['icontains'],
            'numero_serie': ['exact'],
        }