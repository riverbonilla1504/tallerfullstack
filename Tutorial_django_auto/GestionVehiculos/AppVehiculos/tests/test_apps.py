from django.apps import apps 
from django.test import TestCase
from AppVehiculos.apps import AppvehiculosConfig


class AppVehiculosConfigTest(TestCase):
    def test_app_config(self):
        self.assertEqual(AppvehiculosConfig.name , "AppVehiculos")
        self.assertEqual(apps.get_app_config("AppVehiculos").name ,"AppVehiculos")