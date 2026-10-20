from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Usuario

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    # write_only=True significa que la contraseña se recibe, pero nunca se devuelve en la respuesta
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'rol', 'password')

    def create(self, validated_data):
        # Usamos create_user para que Django encripte la contraseña automáticamente (hash)
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            rol=validated_data.get('rol', Usuario.Rol.CONDUCTOR),
            password=validated_data['password']
        )
        return user