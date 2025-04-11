from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from AppVehiculos.models import Vehiculo
from .serializers import VehiculoSerializer

# ---------------------- GESTIÓN DE VEHÍCULOS ----------------------
class VehiculoApiView(APIView):
    

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.AllowAny]


    def get(self, request, placa=None, *args, **kwargs):
       
        if placa:
            vehiculo = get_object_or_404(Vehiculo, placa=placa)
            serializador = VehiculoSerializer(vehiculo)
            return Response({"message": "Vehículo encontrado", "vehiculo": serializador.data}, status=status.HTTP_200_OK)

        vehiculos = Vehiculo.objects.all()
        serializador = VehiculoSerializer(vehiculos, many=True)
        return Response({"message": "Lista de vehículos", "vehiculos": serializador.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Crea un nuevo vehículo"""
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Vehículo registrado exitosamente", "vehiculo": serializer.data}, 
                status=status.HTTP_201_CREATED
            )

        return Response(
            {"error": "Datos inválidos", "detalles": serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, placa, *args, **kwargs):
        """Actualiza un vehículo existente"""
        vehiculo = get_object_or_404(Vehiculo, placa=placa)
        serializer = VehiculoSerializer(vehiculo, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Vehículo actualizado correctamente", "vehiculo": serializer.data}, 
                status=status.HTTP_200_OK
            )

        return Response(
            {"error": "Error en la actualización", "detalles": serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, placa, *args, **kwargs):
        """Elimina un vehículo por su placa"""
        vehiculo = get_object_or_404(Vehiculo, placa=placa)
        vehiculo.delete()
        return Response({"message": "Vehículo eliminado correctamente"}, status=status.HTTP_200_OK)
