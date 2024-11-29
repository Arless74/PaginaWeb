from django.urls import path

from ProyectoWebApp import views
from .views import VRegistro, cerrar_session, logear

urlpatterns = [ #url default de contacto.html

    path('', VRegistro.as_view() , name="Autenticacion"),

    path('cerrar_sesion', cerrar_session , name="cerrar_sesion"),

    path('logear', logear , name="logear"),

]