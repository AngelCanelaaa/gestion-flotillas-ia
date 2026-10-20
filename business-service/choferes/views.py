from rest_framework import mixins, viewsets
from .models import Chofer
from .serializers import ChoferSerializer


class ChoferViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """Solo POST (crear). Listar y filtrar se harán en otra historia."""
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer