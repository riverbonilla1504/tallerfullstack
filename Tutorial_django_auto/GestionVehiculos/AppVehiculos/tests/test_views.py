import json
from django.test import TestCase
from rest_framework import status
from AppVehiculos.models import Vehiculo


class VehiculoApiTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.mi_vehiculo = Vehiculo.objects.create(
            placa='iut123',
            marca='chevrolet',
            color=1,
            modelo=1990
        )

    def test_obtener_todos_los_vehiculos(self):
        response = self.client.get('/api/vehiculo/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("vehiculos", response.json())

    def test_obtener_vehiculo_por_placa(self):
        response = self.client.get(f'/api/vehiculo/{self.mi_vehiculo.placa}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("vehiculo", response.json())
        self.assertEqual(response.json()["vehiculo"]["placa"], self.mi_vehiculo.placa)

    def test_crear_vehiculo(self):
        data = {
            'placa': 'wer123',
            'marca': 'mazda',
            'color': 2,
            'modelo': 2010
        }
        response = self.client.post('/api/vehiculo/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        vehiculo_encontrado = Vehiculo.objects.filter(placa='wer123').first()
        self.assertIsNotNone(vehiculo_encontrado)
        self.assertEqual(vehiculo_encontrado.marca, 'mazda')

    def test_actualizar_vehiculo(self):
        data_actualizada = {
            'marca': 'toyota',
            'color': 3,
            'modelo': 2022
        }
        response = self.client.put(
            f'/api/vehiculo/{self.mi_vehiculo.placa}/',
            data=json.dumps(data_actualizada),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.mi_vehiculo.refresh_from_db()
        self.assertEqual(self.mi_vehiculo.marca, 'toyota')

    def test_eliminar_vehiculo_existente(self):
        response = self.client.delete(f'/api/vehiculo/{self.mi_vehiculo.placa}/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Vehiculo.objects.filter(placa=self.mi_vehiculo.placa).exists())

    def test_crear_vehiculo_datos_invalidos(self):
        data_invalida = {
            'marca': 'toyota',
            'color': 1,
            'modelo': 2020
        }
        response = self.client.post('/api/vehiculo/', data_invalida)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('detalles', response.json())

    def test_eliminar_vehiculo_inexistente(self):
        response = self.client.delete('/api/vehiculo/zz999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.json())
