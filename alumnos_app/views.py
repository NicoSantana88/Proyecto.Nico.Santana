from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import PostForm
# Create your views here.




def estudiantes_list(request):
    '''La Clave que paso en contex es la que se va a usar en el html'''
    estudiantes_list= Estudiante.objects.all()
    return render(request, "alumnos_app/lista_Alumnos.html", context={"estudiantes_list": estudiantes_list})


def post_create(request):
    if request.method == "POST":
        form= PostForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            if request.user.is_authenticated:
                post.autor= request.user
                post.save()
                return redirect("alumnos_app:estudiantes")
            else:
                form.add_error(None,"Debes estar logueado para crear un nuevo Alumno")
    else:
        form= PostForm()
    
    return render(request, "alumnos_app/post_alumnos.html", context={"form": form})
    
