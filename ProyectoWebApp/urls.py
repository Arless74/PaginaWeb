from django.urls import path

from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="Home"), #el path es el inicial por eso es el ''

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#Renderiza la servicios.html y trae todo lo de la clase servicios

