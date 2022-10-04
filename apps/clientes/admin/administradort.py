from django.contrib import admin 
#ESTO LOS QUE MUESTRA EN ADMIN PARA ADMINISTRAR EL DESDE EL SUPER USUARIO
from apps.clientes.models.cliente import Cliente
from apps.clientes.models.producto import Producto
from apps.clientes.models.ventas import Ventas

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    
    list_display = [
        'nombres',
        'apellidos',
        'numero_identidad',
        'fecha_nacimiento',
        'ingreso_mensual',
    ]

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    
    list_display = [
        'nombres',
        'precio',
    ]

@admin.register(Ventas)
class VentasAdmin(admin.ModelAdmin):
    
    list_display = [
        'facturas',
        'fecha_venta',
    ]
