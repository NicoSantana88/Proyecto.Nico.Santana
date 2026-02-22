from django.shortcuts import render
#from django.http import HttpResponse
#from .models import Estudiante
# Create your views here. maneja las logicas


def indexPrueba(request):
    '''en render, request siempre va, la ubicacion a donde va a ir y el tercer dato es el context, un diccionario '''
    context={"mensaje2" : "Bienvenidos al sito"}
    return render (request, "myapp/base.html", context) 

#def saludar (request, nombre: str, apellido: str):
 #   nombre= nombre.capitalize()
  #  apellido= apellido.capitalize()
    
   # return HttpResponse(f"Respuesta para {nombre} con el apellido {apellido}")#al no aclarar que va a myapp/index.html al correr http://127.0.0.1:8000/saludo me muestra solo el mensaje



