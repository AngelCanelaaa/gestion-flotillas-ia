from rest_framework import viewsets
from .models import Ruta
from .serializers import RutaSerializer

class RutaViewSet(viewsets.ModelViewSet):
    """CRUD completo para Rutas (GET, POST, PUT, DELETE)"""
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer