from django.shortcuts import render
from .models import Estudiante
# Create your views here.




def estudiantes_list(request):
    '''La Clave que paso en contex es la que se va a usar en el html'''
    estudiantes_list= Estudiante.objects.all()
    return render(request, "alumnos_app/lista_Alumnos.html", context={"estudiantes_list": estudiantes_list})