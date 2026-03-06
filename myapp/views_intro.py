from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from .models import Estudiante
# Create your views here. maneja las logicas
from django.contrib.auth.decorators import login_required
from .forms import EditUserForm, MiRegistro
from django.views.generic import CreateView
from django.urls import reverse_lazy

def logeo(request):
    
        
    return render(request, "myapp/navbar.html")
    

def indexPrueba(request):
    '''en render, request siempre va, la ubicacion a donde va a ir y el tercer dato es el context, un diccionario '''
    context={"mensaje2" : "Bienvenidos al sito"}
    return render (request, "myapp/index.html", context) 


def perfil(request):
    
    return render(request, "myapp/perfil.html")


@login_required
def editar_perfil(request):
    if request.method =="POST":
        form= EditUserForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect ("myapp:perfil")
        
        else:
            form= EditUserForm( instance= request.user)
    return render(request, "myapp/editar_perfil.html", {"form":form})
        
            
class Register(CreateView):
    form_class= MiRegistro
    template_name="myapp/register.html"
    success_url= reverse_lazy("myapp:login")
    

