from rest_framework import mixins, viewsets
from .models import Vehiculo
from .serializers import VehiculoSerializer
from .filters import VehiculoFilter

class VehiculoViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,     # <-- Permite GET (listar)
    mixins.RetrieveModelMixin, # <-- Permite GET por ID (ej. /api/vehiculos/1/)
    viewsets.GenericViewSet,
):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    filterset_class = VehiculoFilter # <-- Conecta los filtros