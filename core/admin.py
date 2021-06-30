from django.contrib import admin
from .models import Especialidad, Medico, reserva, Hora, Boleta

# Register your models here.



class EspecialidadAdmin(admin.ModelAdmin):
    list_display = (
        'especialidad',
        'monto',
    )
        
    

admin.site.register(Especialidad, EspecialidadAdmin)



class MedicoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'rutM',
        'nombreM',
        'apellidosM',
        'especialidad',
    )
admin.site.register(Medico, MedicoAdmin)


class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'rut',
        'nombre',
        'apellidos',
        'correo',
        'fecha_nacimiento',
        'sexo',
        'fecha_hora',
        'monto',
    )
admin.site.register(reserva, ReservaAdmin)
    

class HoraAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fullHora',
        'Medico',
        'Especialidad',
        'Costo',
        'tomada',
    )
    def fullHora(self, obj):
        return str(obj.fecha_reservaR) + ' ' + str(obj.horaR)
    
    def Medico(self, obj):
        return str(obj.medico.id) + ' ' + str(obj.medico.nombreM)

    def Especialidad(self, obj):
        return str(obj.medico.especialidad.especialidad)

    def Costo(self, obj):
        return str(obj.medico.especialidad.monto)

admin.site.register(Hora, HoraAdmin)


class BoletaAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nro_reserva',
    )

admin.site.register(Boleta, BoletaAdmin)


