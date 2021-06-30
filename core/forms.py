from django import forms
from django.forms import widgets

from .models import reserva

class ReservaForm(forms.ModelForm):

    class Meta:
        model = reserva

        fields = [
            'rut',
            'nombre',
            'apaterno',
            'amaterno',
            'correo',
            'fecha_nacimiento',
            'sexo',
            'nombreM',
            'fecha_reservaR',
            'montoR',
            'horaR',
            'especialidad',
        ]
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'apaterno': 'Apaterno',
            'amaterno': 'Amaterno',
            'correo': 'Correo',
            'fecha_nacimiento': 'Fecha nacimiento',
            'sexo': 'Sexo',
            'nombreM': 'Nombre medico',
            'fecha_reservaR': 'Fecha reserva',
            'montoR': 'Monto reserva',
            'horaR': 'Hora reserva',
            'especialidad': 'Especialidad',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class':'formulario__input'}),
            'nombre': forms.TextInput(attrs={'class':'formulario__input'}),
            'apaterno': forms.TextInput(attrs={'class':'formulario__input'}),
            'amaterno': forms.TextInput(attrs={'class':'formulario__input'}),
            'correo': forms.TextInput(attrs={'class':'formulario__input'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'formulario__input'}),
            'sexo': forms.TextInput(attrs={'class':'formulario__input'}),
            'nombreM': forms.Select(attrs={'Class':'formulario__input'}),
            'fecha_reservaR': forms.Select(attrs={'Class':'formulario__input'}),
            'montoR': forms.Select(attrs={'Class':'formulario__input'}),
            'horaR': forms.Select(attrs={'Class':'formulario__input'}),
            'especialidad': forms.Select(attrs={'Class':'formulario__input'}),
        }