from django.db import models

# Create your models here.

class Servicio(models.Model): #define una clase llamada servicio y a la vez crea un tabla en la db
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta: #Mostrar modelo mucho mejor
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self): #Mostrar la cadena legible
        return self.titulo
