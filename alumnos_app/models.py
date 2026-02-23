from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Estudiante(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    direccion= models.TextField()#Otro tipo de texto
    email =models.EmailField()
    autor= models.ForeignKey(User, on_delete=models.CASCADE)#Saber que usario creo cada dato
    def __str__(self):
        return f"{self.nombre} {self.apellido}"