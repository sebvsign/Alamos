from django.urls import path

from .views import home, diario, login_medico, login_secretaria, vistamedico, paciente, recaudo, total, reserva_view#,homepacientes

from . import views

urlpatterns = [
    path('', home, name="home"),
    path('diario/', diario, name="diario"),
    #path('homepacientes/', homepacientes, name="homepacientes"),
    path('login_medico/', login_medico, name="login_medico"),
    path('login_secretaria/', login_secretaria, name="login_secretaria"),
    path('vistamedico/', vistamedico, name="vistamedico"),
    path('paciente/', paciente, name="paciente"),
    path('recaudo/', recaudo, name="recaudo"),
    path('total/', total, name="total"),
    #path('reserva/', views.PacienteCreateView.as_view(), name='reserva'),
    path('reserva/', reserva_view , name='reserva'),
]