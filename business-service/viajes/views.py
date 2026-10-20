from rest_framework import mixins, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Viaje
from .serializers import ViajeSerializer
from core.mongo import get_mongo_db

class ViajeViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """Solo POST (crear)."""
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer

class GenerarResumenViajeView(APIView):
    """Genera el documento analítico en MongoDB para un viaje."""
    def post(self, request, viaje_id):
        viaje = get_object_or_404(Viaje, id=viaje_id)
        
        # 1. Obtener datos de PostgreSQL (Incidentes)
        incidentes = viaje.incidentes.all()
        total_episodios = incidentes.count()
        
        # Calcular críticos (nivel_riesgo == 'alto' o 'critico')
        episodios_criticos = incidentes.filter(nivel_riesgo__in=['alto', 'critico']).count()
        
        # Distribución por tipo
        distribucion = {
            'ojo_cerrado': incidentes.filter(tipo='ojo_cerrado').count(),
            'bostezo': incidentes.filter(tipo='bostezo').count(),
        }
        
        # Duración total de alertas
        duracion_total = sum(inc.duracion_episodio_seg for inc in incidentes)
        
        # Cálculo simple de score (puedes mejorarlo después)
        score_riesgo = min(1.0, (episodios_criticos * 0.3) + (total_episodios * 0.1))

        # 2. Construir el documento para MongoDB
        resumen_doc = {
            "viaje_id": viaje.id,
            "chofer_id": viaje.chofer.id,
            "total_episodios": total_episodios,
            "episodios_criticos": episodios_criticos,
            "distribucion": distribucion,
            "duracion_total_alertas_seg": duracion_total,
            "score_riesgo_viaje": round(score_riesgo, 2),
            "fecha_generado": "2026-10-20T00:00:00Z" # En un caso real usarías datetime.now(timezone.utc)
        }

        # 3. Guardar en MongoDB (usamos upsert para que si ya existe, lo actualice)
        db = get_mongo_db()
        coleccion = db['resumen_viaje']
        coleccion.update_one(
            {"viaje_id": viaje.id}, 
            {"$set": resumen_doc}, 
            upsert=True
        )

        return Response(
            {"mensaje": "Resumen generado exitosamente en MongoDB", "data": resumen_doc}, 
            status=status.HTTP_201_CREATED
        )