from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Usuario

class UsuarioAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/auth/register/'
        self.valid_payload = {
            "username": "testuser",
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "rol": "conductor",
            "password": "SuperSecretPassword123!"
        }

    def test_registro_usuario_exitoso(self):
        """Prueba que un usuario puede registrarse correctamente"""
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.count(), 1)
        self.assertEqual(Usuario.objects.get().username, 'testuser')

    def test_registro_password_debil(self):
        """Prueba que una contraseña débil es rechazada"""
        invalid_payload = self.valid_payload.copy()
        invalid_payload['password'] = '123'
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)