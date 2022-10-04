from django.db import models

from apps.clientes.models.cliente import Cliente
from apps.clientes.models.producto import Producto

class Ventas(models.Model):
    facturas = models.CharField(
        verbose_name = 'nombres de factura',
        #help_text = 'nombre de clientes',
        max_length = 200
    )
    fecha_venta = models.DateField(
        verbose_name = 'fecha de venta',
        #help_text = 'fecha de nacimiento',
        max_length = 11,
        blank = True, null = True
    )
    
    
    #Relacion de tablas cliente, producto



    cliente_fk = models.ForeignKey(Cliente, on_delete= models.SET_NULL, null = True)
    producto_fk = models.ForeignKey(Producto, on_delete= models.SET_NULL, null = True)

    
    def __str__(self):
        return self.facturas
    
    class Meta:
        app_label = 'clientes'
        db_table = 'ventas'
        verbose_name = "Venta"
        verbose_name_plural = "Ventas" 
        
    