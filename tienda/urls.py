from django.urls import path

from . import views #importo desde la misma carpeta

urlpatterns = [
    path('',views.tienda, name="Tienda"), #path de la tienda

]