from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UsuarioRegistroSerializer
from .models import Usuario

class RegistroUsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioRegistroSerializer
    # AllowAny permite que cualquiera se registre sin necesidad de estar logueado
    permission_classes = [AllowAny] 