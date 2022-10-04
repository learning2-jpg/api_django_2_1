
from rest_framework import serializers
from apps.clientes.models import Cliente

class ClienteSerializer2(serializers.ModelSerializer):
    #esre el serializer para el modelo Cliente
    class Meta:
        model = Cliente
        fields = [
            'nombres',
            'apellidos',
            'numero_identidad',
            'fecha_nacimiento',
            'ingreso_mensual',
        ]
        