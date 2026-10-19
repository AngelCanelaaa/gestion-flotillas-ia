from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from django.shortcuts import get_object_or_404
from .serializers import DeteccionFatigaSerializer, IncidenteSerializer, IncidenteHistorialSerializer
from .models import Incidente
from core.mongo import get_mongo_db

# --- Vista de MongoDB (SCRUM-13) ---
class DeteccionFatigaCreateView(APIView):
    def post(self, request):
        serializer = DeteccionFatigaSerializer(data=request.data)
        
        if serializer.is_valid():
            db = get_mongo_db()
            coleccion = db['detecciones_fatiga']
            coleccion.insert_one(serializer.validated_data)
            
            return Response(
                {"mensaje": "Detección guardada exitosamente en MongoDB", "episodio_id": serializer.validated_data['episodio_id']}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- Vistas de PostgreSQL (SCRUM-14) ---
class IncidenteViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

class IncidenteHistorialView(APIView):
    """Endpoint para obtener el historial de un incidente específico."""
    def get(self, request, incidente_id):
        incidente = get_object_or_404(Incidente, id=incidente_id)
        historial = incidente.historial.all()
        serializer = IncidenteHistorialSerializer(historial, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)