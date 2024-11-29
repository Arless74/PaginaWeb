from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage

# Create your views here.
def contacto(request): #Metodo que sirve para envio de Correo 
    formulario_contacto=FormularioContacto() #Instanciamiento del metodo FormularioContacto

    if request.method == "POST": #Si el metodo es POST 
        formulario_contacto=FormularioContacto(data=request.POST) # Se obtendran los datos ingresados en el formularios 
        if formulario_contacto.is_valid(): #Si los datos del formulario son correcto
            nombre=request.POST.get("nombre") #obtener nombre
            email=request.POST.get("email") #obtener mail
            contenido=request.POST.get("contenido") #obtener el contenido

            email=EmailMessage("Mensaje desde App Django",
                               "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n{}".format(nombre.email,contenido),
                               "",["alexadasme74@gmail.com"],reply_to=[email]) # creador del mensaje de email
            
            try: #try para envio de email

                email.send() # envio de email
                return redirect("/contacto/?valido") #enviar una pantalla de respuesta al cliente Positiva
            
            except:
                return redirect("/contacto/?novalido")#enviar una pantalla de respuesta al cliente Negativa       

    return render(request,'contacto/contacto.html',{'miFormulario':formulario_contacto}) #renderizacion del contacto.html y del formulario



