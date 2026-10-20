from rest_framework import serializers
from .models import Viaje
from mantenimientos.models import Mantenimiento

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = '__all__'
        read_only_fields = ['id', 'creado_en', 'actualizado_en']

    def validate(self, data):
        # Regla 1: Un chofer no puede tener dos viajes en_curso a la vez
        if data.get('estado') == Viaje.Estado.EN_CURSO:
            chofer = data.get('chofer')
            if Viaje.objects.filter(chofer=chofer, estado=Viaje.Estado.EN_CURSO).exists():
                raise serializers.ValidationError(
                    {"chofer": "Este chofer ya tiene un viaje en curso. Debe finalizarlo antes de iniciar otro."}
                )

        # Regla 2: Un vehículo con mantenimiento abierto no puede asignarse a un viaje
        vehiculo = data.get('vehiculo')
        if vehiculo:
            mantenimiento_abierto = Mantenimiento.objects.filter(
                vehiculo=vehiculo, 
                estado=Mantenimiento.Estado.ABIERTO
            ).exists()
            
            if mantenimiento_abierto:
                raise serializers.ValidationError(
                    {"vehiculo": "Este vehículo tiene un mantenimiento abierto. No puede asignarse a un viaje."}
                )

        return data