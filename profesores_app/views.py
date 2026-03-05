from django.shortcuts import render, redirect

# Create your views here.
from .models import Profesor
# Create your views here.
from .forms import PostForm



def profesor_list(request):
    '''La Clave que paso en contex es la que se va a usar en el html'''
    #profesor_list= Profesor.objects.all()
    #return render(request, "profesor_app/lista_Profesores.html", context={"profesor_list": profesor_list})

    busqueda= request.GET.get("busqueda", None)#Nuevo
    if busqueda:
        profesor_list= Profesor.objects.filter(apellido__icontains=busqueda)
    else:
        profesor_list= Profesor.objects.all()
    return render(request, "profesores_app/lista_Profesores.html", context={"profesor_list": profesor_list})



def post_profesor(request):
    if request.method == "POST":
        form= PostForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            if request.user.is_authenticated:
                post.autor= request.user
                post.save()
                return redirect("profesores_app:Profesores")
            else:
                form.add_error(None,"Debes estar logueado para crear un nuevo Profesor")
    else:
        form= PostForm()
    
    return render(request, "profesores_app/post_profesores.html", context={"form": form})