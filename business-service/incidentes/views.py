from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DeteccionFatigaSerializer
from core.mongo import get_mongo_db

class DeteccionFatigaCreateView(APIView):
    def post(self, request):
        serializer = DeteccionFatigaSerializer(data=request.data)
        
        if serializer.is_valid():
            db = get_mongo_db()
            coleccion = db['detecciones_fatiga']
            
            # Guardar el documento en MongoDB
            coleccion.insert_one(serializer.validated_data)
            
            return Response(
                {"mensaje": "Detección guardada exitosamente en MongoDB", "episodio_id": serializer.validated_data['episodio_id']}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)