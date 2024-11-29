from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.servicios, name="Servicios"), #deja como inicial el path para traer el html servicios
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # sirve para traer tanto imagenes u archivos
