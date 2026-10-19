from rest_framework import serializers

class DeteccionFatigaSerializer(serializers.Serializer):
    episodio_id = serializers.CharField(max_length=50)
    chofer_id = serializers.IntegerField()
    viaje_id = serializers.IntegerField()
    timestamp_inicio = serializers.DateTimeField()
    timestamp_fin = serializers.DateTimeField()
    tipo = serializers.ChoiceField(choices=['ojo_cerrado', 'bostezo'])
    duracion_episodio_seg = serializers.FloatField()
    confianza_maxima = serializers.FloatField()
    modelo_version = serializers.CharField(max_length=20)
    truncado_por_duracion_maxima = serializers.BooleanField()
    muestras = serializers.ListField(child=serializers.DictField(), required=False, default=[])
    frame_referencia_url = serializers.CharField(allow_null=True, required=False, default=None)