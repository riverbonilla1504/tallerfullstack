import re  # 🔹 Se añadió la importación faltante
from rest_framework import serializers
from AppVehiculos.models import Vehiculo  # 🔹 Se eliminó la importación de CustomUser

# 🔹 SERIALIZADOR DE VEHÍCULO
class VehiculoSerializer(serializers.ModelSerializer):
    color = serializers.CharField(source='get_color_display', read_only=True)

    class Meta:
        model = Vehiculo
        fields = ['id', 'placa', 'marca', 'color', 'modelo']

    def validate_placa(self, value):
        """Validar que la placa tenga el formato correcto (Ejemplo: ABC123)."""
        value = value.strip().upper()  # 🔹 Elimina espacios y normaliza a mayúsculas
        if not re.match(r'^[A-Z]{3}\d{3}$', value):
            raise serializers.ValidationError("Formato de placa inválido. Debe ser 3 letras seguidas de 3 números (Ejemplo: ABC123).")
        return value

    def validate_modelo(self, value):
        """Validar que el modelo no sea menor a 1900."""
        if value < 1900:
            raise serializers.ValidationError("El modelo del vehículo no puede ser menor a 1900.")
        return value
