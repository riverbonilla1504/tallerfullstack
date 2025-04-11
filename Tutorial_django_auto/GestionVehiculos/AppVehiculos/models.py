from django.db import models
# Modelo de Vehículo
class Vehiculo(models.Model):
    COLORLIST = (
        ('ROJO', 'Rojo'),
        ('AZUL', 'Azul'),
        ('VERDE', 'Verde'),
    )
    placa = models.CharField(max_length=6, unique=True)
    marca = models.CharField(max_length=10)
    color = models.CharField(max_length=10, choices=COLORLIST)
    modelo = models.IntegerField()

    def __str__(self):
        return f"{self.marca} ({self.placa})"
