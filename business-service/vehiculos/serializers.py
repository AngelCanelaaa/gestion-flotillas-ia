from rest_framework import serializers
from .models import Vehiculo


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        read_only_fields = ['id', 'creado_en', 'actualizado_en']

    def validate_numero_serie(self, value):
        if len(value) != 17:
            raise serializers.ValidationError(
                'El VIN debe tener exactamente 17 caracteres.'
            )
        return value

    def validate_capacidad(self, value):
        if value <= 0:
            raise serializers.ValidationError('La capacidad debe ser mayor a cero.')
        return value