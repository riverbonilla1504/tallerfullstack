from django.urls import path
from .views import VehiculoApiView

urlpatterns = [
    path('', VehiculoApiView.as_view(), name='vehiculo-list-create'),
    path('<str:placa>/', VehiculoApiView.as_view(), name='vehiculo-detail'),
]
