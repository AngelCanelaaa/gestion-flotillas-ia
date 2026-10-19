from rest_framework import serializers
from .models import Chofer


class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chofer
        fields = '__all__'
        read_only_fields = ['id', 'creado_en', 'actualizado_en']