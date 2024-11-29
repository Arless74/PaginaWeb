from django.shortcuts import render

from .models import Producto

# Create your views here.



def tienda(request): #Metodo que redirige a la pagina tienda

    productos=Producto.objects.all()

    return render(request,'tienda/tienda.html',{"productos":productos}) #Renderiza la tienda.html
