from pyexpat import model
from tabnanny import verbose
from django.db import models

class Producto(models.Model):
    nombres = models.CharField(
        verbose_name = 'nombres',
        #help_text = 'nombre de clientes',
        max_length = 200
    )
    
    precio = models.DecimalField(
        verbose_name = 'precio de producto',
        #help_text = 'monto de ingrso',
        decimal_places = 2,
        max_digits = 10,
        blank = True, null = True
    )
    
    def __str__(self):
        return self.nombres
    
    class Meta:
        app_label = 'clientes'
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        