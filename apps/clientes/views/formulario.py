from logging import PlaceHolder

from django.forms import ModelForm
from apps.clientes.models import Cliente

from django import forms
from django.forms import TextInput, EmailInput

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields =['nombres','apellidos','numero_identidad','fecha_nacimiento','ingreso_mensual']
        labels = {
            'nombres': 'Nombre de usuario',
            'apellidos': 'Apellidos del cliente',
            'numero_identidad':'N° de Ci',
            'fecha_nacimiento':'fecha de nacimiento',
            'ingreso_mensual':'Ingreso mensual del cliente',
        }
        
        
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_identidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'ingreso_mensual': forms.TextInput(attrs={'class': 'form-control'}),
        }
    