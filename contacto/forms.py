from django import forms

class FormularioContacto(forms.Form): #estructuracion del formulario utilizando la libreria forms

    nombre= forms.CharField(label="Nombre", required=True)
    email= forms.EmailField(label="Email", required=True) 
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)