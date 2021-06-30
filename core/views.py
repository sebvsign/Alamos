from django.shortcuts import render, redirect
from .models import Especialidad,Medico, reserva, Hora
from django.views.generic import CreateView
# Create your views here.

from core.forms import ReservaForm
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def diario(request):
    return render(request, 'core/diario.html')

#class PacienteCreateView(CreateView):
#        template_name = 'core/reserva.html'
#        model = reserva
#        fields = ('__all__')
#        success_url = '.'

def reserva_view(request):

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('core:reserva')
    else:
        form = ReservaForm()
    return render(request, 'core/reserva.html', {'form':form})



#def homepacientes(request):

    

    #return render(pacienteCreateView)


    #especialidad , medico, monto, fecha, hora = Especialidad.objects.all, Medico.objects.all, Hora.objects.all, Hora.objects.all, Hora.objects.all

    #variables = {
    #    'especialidad': especialidad,
    #    'medico': medico,
    #    'monto': monto,
    #    'fecha': fecha,
    #    'hora': hora
        
    #}

    #if request.POST:
    #    Reserva = reserva()
    #    Reserva.rut = request.POST.get('rut')
    #    Reserva.nombre = request.POST.get('nombre')
    #    Reserva.apaterno = request.POST.get('paterno')
    #    Reserva.amaterno = request.POST.get('materno')
    #    Reserva.correo = request.POST.get('correo')
    #    Reserva.fecha_nacimiento = request.POST.get('fechaNacimiento')
    #    Reserva.sexo = request.POST.get('sexo')
        #especialidad = Especialidad
        #Especialidad.id = request.POST.get('especialidad')
        #medico = Medico()
        #Medico.id = request.POST.get('servicio')
        #monto = Hora()
        #Hora.montoR = request.POST.get('monto')
        #fecha = Hora()
        #Hora.fecha_reservaR = request.POST.get('fecha')
        #hora = Hora()
        #Hora.horaR = request.POST.get('hora')
        
        #try:
        #    Reserva.save()
            #variables['mensaje'] = 'guardado correcctamente'
        #except:
            #variables['mensaje'] = 'error al guardar'
            
    #return render(request, 'core/homepacientes.html',variables)

#class ReservaCreateView(CreateView):
 #   template_name = 'core/homepaciente.html'
 #   model = reserva
 #   fields = '__all__'
    

def login_medico(request):
    return render(request, 'core/login_medico.html')

def login_secretaria(request):
    return render(request, 'core/login_secretaria.html')

def vistamedico(request):
    return render(request, 'core/vistamedico.html')

def paciente(request):
    return render(request, 'core/paciente.html')

def recaudo(request):
    return render(request, 'core/recaudo.html')

def total(request):
    return render(request, 'core/total.html')