from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def servicios(request):

    servicios= Servicio.objects.all() #trae todas las variables de la clase Servicios
    return render(request,'servicios/servicios.html', {"servicios": servicios}) #Renderiza la servicios.html y trae todo lo de la clase servicios

