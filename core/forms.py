from django import forms
from django.forms import widgets

from .models import reserva

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservaForm(forms.ModelForm):

    class Meta:
        model = reserva

        fields = ('__all__')
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'correo': 'Correo',
            'fecha_nacimiento': 'Fecha nacimiento',
            'sexo': 'Sexo',
            'fecha_hora': 'Fecha Hora',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class':'formulario__input'}),
            'nombre': forms.TextInput(attrs={'class':'formulario__input'}),
            'apellidos': forms.TextInput(attrs={'class':'formulario__input'}),
            'correo': forms.TextInput(attrs={'class':'formulario__input'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'formulario__input'}),
            'sexo': forms.Select(attrs={'Class':'formulario__input'}),
            'nombreM': forms.Select(attrs={'Class':'formulario__input'}),
            'fecha_reservaR': forms.Select(attrs={'Class':'formulario__input'}),
            
        }