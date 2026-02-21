from django.shortcuts import render

# Create your views here. maneja las logicas

def index(request):
    '''en render, request siempre va, la ubicacion a donde va a ir y el tercer dato es el context, un diccionario '''
    context={"mensaje" : "Bienvenidos al sito"}
    return render (request, "myapp/index.html", context) 