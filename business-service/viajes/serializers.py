from rest_framework import serializers
from .models import Viaje


class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = '__all__'
        read_only_fields = ['id', 'creado_en', 'actualizado_en']

    def validate(self, data):
        # Regla de negocio: Un chofer no puede tener dos viajes en_curso a la vez
        if data.get('estado') == Viaje.Estado.EN_CURSO:
            chofer = data.get('chofer')
            viaje_activo = Viaje.objects.filter(
                chofer=chofer, 
                estado=Viaje.Estado.EN_CURSO
            ).exists()
            
            if viaje_activo:
                raise serializers.ValidationError(
                    {"chofer": "Este chofer ya tiene un viaje en curso. Debe finalizarlo antes de iniciar otro."}
                )
        return data