from pyexpat import model
from tabnanny import verbose
from django.db import models

class Cliente(models.Model):
    nombres = models.CharField(
        verbose_name = 'nombres',
        #help_text = 'nombre de clientes',
        max_length = 200
    )
    apellidos = models.CharField(
        verbose_name = 'apellidos',
        #help_text = 'apellidos de clientes',
        max_length = 254
    )
    numero_identidad = models.CharField(
        verbose_name = 'numero de identidad',
        #help_text = 'numero identidad',
        max_length = 10
    )
    fecha_nacimiento = models.DateField(
        verbose_name = 'fecha de namiento',
        #help_text = 'fecha de nacimiento',
        max_length = 11,
        blank = True, null = True
    )
    ingreso_mensual = models.DecimalField(
        verbose_name = 'monto de ingreso',
        #help_text = 'monto de ingrso',
        decimal_places = 2,
        max_digits = 10,
        blank = True, null = True
    )
    
    def __str__(self):
        return self.nombres
    
    class Meta:
        app_label = 'clientes'
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        