from django.shortcuts import render
from django.http import HttpResponse
from .models import Estudiante
# Create your views here. maneja las logicas

def index(request):
    '''en render, request siempre va, la ubicacion a donde va a ir y el tercer dato es el context, un diccionario '''
    context={"mensaje" : "Bienvenidos al sito"}
    return render (request, "myapp/index.html", context) 

def saludar (request, nombre: str, apellido: str):
    nombre= nombre.capitalize()
    apellido= apellido.capitalize()
    
    return HttpResponse(f"Respuesta para {nombre} con el apellido {apellido}")#al no aclarar que va a myapp/index.html al correr http://127.0.0.1:8000/saludo me muestra solo el mensaje

def estudiantes_list(request):
    estudiantes_list= Estudiante.objects.all()
    return render(request, "myapp/lista_Alumnos.html", context={"estudiantes_list": estudiantes_list})

