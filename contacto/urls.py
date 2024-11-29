from django.urls import path

from ProyectoWebApp import views
from . import views

urlpatterns = [ #url default de contacto.html

    path('',views.contacto, name="Contacto"),

]