from django.contrib import admin
from .models import Servicio

# Register your models here.
class ServiciosAdmin(admin.ModelAdmin):  #Modelo que dice que se podra leer el created y updated
    readonly_fields=('created','updated')

admin.site.register(Servicio,ServiciosAdmin)