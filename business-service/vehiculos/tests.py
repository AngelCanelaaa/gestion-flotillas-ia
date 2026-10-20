from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Vehiculo

class VehiculoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/vehiculos/'
        self.valid_payload = {
            "numero_serie": "1HGCM82633A000001",
            "placa": "TEST-001",
            "marca": "TestMarca",
            "modelo": "TestModelo",
            "capacidad": 500,
            "odometro_km": 100.0
        }

    def test_crear_vehiculo_exitoso(self):
        """Prueba que se puede crear un vehículo válido"""
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vehiculo.objects.count(), 1)

    def test_crear_vehiculo_vin_invalido(self):
        """Prueba que no se permite un VIN con longitud incorrecta"""
        invalid_payload = self.valid_payload.copy()
        invalid_payload['numero_serie'] = 'CORTO'
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)