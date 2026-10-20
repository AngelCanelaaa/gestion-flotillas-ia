from rest_framework import mixins, viewsets
from .models import Mantenimiento
from .serializers import MantenimientoSerializer

class MantenimientoViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer