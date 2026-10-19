from rest_framework import mixins, viewsets
from .models import Vehiculo
from .serializers import VehiculoSerializer


class VehiculoViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """Solo POST (crear). Listar y filtrar son SCRUM-10."""
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer