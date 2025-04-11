import json 
from django.test import TestCase
from django.urls import reverse 
from rest_framework import status
from AppVehiculos.models import vehiculo

class test_vehicle(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mi_vehiculo=vehiculo.objects.create(
            placa='iut123',
            marca='chevrolet',
            color='1',
            modelo='1990'
        )

    def tearDown(self):
            pass
    def test_view_vehiculo_obtener_todos(self):
        response=self.cliente.get('/api/vehiculo/obtener-todos')
        data=json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code,200)
        self.assertGreater(len(data),0)

    def test_crear_vehiculo(self):
         response=self.client.post(
              '/api/vehiculo/crear',
              data={
                   'placa':'wer123',
                   'marca':'mazda',
                   'color':'1',
                   'modelo':'1990'
              }

         )
         self.assertIn(response.status_code, [200,201])
         vehiculo_encontrado=vehiculo.objects.filter(placa='wer123').first()
         self.assertEqual(vehiculo_encontrado.marca, 'mazda')


    def test_update_vehiculo(self):
        mi_vehiculo=vehiculo.objects.create(
              placa='ucq123',
              marca='chevrolet',
              color='1',
              modelo='1990'
            
         )
        vehiculo_valido ={
              'placa': 'XYZ456',
              'marca':'Honda',
              'color':'azul',
              'modelo':'1998',
         }
        url=reverse('actualizar_vehiculo ', kwargs={'pkid': mi_vehiculo.id})
        valid_vehicle_json = json.dumps(vehiculo_valido)
        response  =self.client.put (url, valid_vehicle_json, content_type='application/json')
        self.assertIn(response.status_code, [200, 201])

    def test_delete_existing_vehicle(self):
        url= reverse ('eliminar_vehiculo', kwargs={'pkid': self.mi_vehiculo.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(vehiculo.objects.filter(id=self.mi_vehiculo.id).exists())

    def test_post_invalid_data(self):
        invalid_data ={
              'marca':'toyota',
              'color': 1,
              'modelo': 2020
         }
        response =self.client.post('/api/vehiculo/crear', data=invalid_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn('placa', response.data)
        
    def test_delete_nonexistent_vehicle(self):
        nonexistent_url= reverse('eliminar_vehiculo', kwargs={'pkid':9999})
        response =self.client.delete(nonexistent_url)
        self.assertEqual(response.status_code, status.HTTP_404NOT_FOUND)
        self.assertEqual(response.data ('error'),'Vehiculo no encontrado')