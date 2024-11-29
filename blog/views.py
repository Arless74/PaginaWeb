from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

def blog(request): #Metodo que trae todo de la clase Post y lo carga en el render

    posts= Post.objects.all()
    return render(request,'blog/blog.html', {"posts":posts})

def categoria(request, categoria_id):  #Metodo que trae todo de la clase Post y Categoria y lo carga en el render

    categoria = Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categoria=categoria)

    return render(request, 'blog/categoria.html',{"categoria":categoria, "posts":posts})