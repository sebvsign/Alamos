from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Especialidad(models.Model):
    especialidad = models.CharField(max_length=80)

    def __str__(self):
        return self.especialidad

class Medico(models.Model):
    rutM = models.CharField(max_length=11)
    nombreM = models.CharField(max_length=80)
    apellidosM = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreM + self.apellidosM

class Hora(models.Model):
    fecha_reservaR = models.DateField()
    horaR = models.TimeField()
    medico = models.ForeignKey(Medico, on_delete= models.CASCADE)
    monto = models.FloatField(null=True, blank=True)
    tomada = models.BooleanField(null = True)
    

    def __str__(self):
        return str(self.id)+ ' - ' + ' fecha: '+ str(self.fecha_reservaR) + '| | '+ str(self.horaR) + str(self.medico)
    

class reserva(models.Model):

    SEXO_CHOICES = (
        ('0', 'Masculino'),
        ('1', 'Femenino')
        ('2', 'Otro'),
    )
    rut = models.CharField('rut', max_length=11)
    nombre = models.CharField('Nombres',max_length=80)
    apellidos = models.CharField('Apellidos',max_length=100)
    correo = models.EmailField('Correo',max_length = 200)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField('Sexo', max_length=1, Choices = SEXO_CHOICES)
    fecha_hora = models.ForeignKey(Hora, on_delete= models.CASCADE)
    montoR = models.ForeignKey(Hora, on_delete=models.CASCADE, related_name= 'monto')
    
    
class Boleta(models.Model):
    nro_reserva = models.ForeignKey(reserva.id, on_delete= models.CASCADE, related_name='id reserva')
    rut = models.ForeignKey(reserva.rut, on_delete= models.CASCADE, related_name='rut paciente')

    

    