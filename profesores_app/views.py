from django.shortcuts import render

# Create your views here.
from .models import Profesor
# Create your views here.




def profesor_list(request):
    '''La Clave que paso en contex es la que se va a usar en el html'''
    profesor_list= Profesor.objects.all()
    return render(request, "profesor_app/lista_Profesores.html", context={"profesor_list": profesor_list})