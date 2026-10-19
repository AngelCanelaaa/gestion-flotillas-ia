from rest_framework import mixins, viewsets
from .models import Viaje
from .serializers import ViajeSerializer


class ViajeViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """Solo POST (crear)."""
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer