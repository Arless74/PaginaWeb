from django.contrib import admin
from .models import Categoria, Post

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin): #Creando campos solo de lectura en las categorias(Pag admin)
    readonly_fields=('created','updated') #Solo Lectura

class PostAdmin(admin.ModelAdmin):#Creando campos solo de lectura en las Post(Pag admin)
     readonly_fields=('created','updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)