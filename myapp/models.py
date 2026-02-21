from django.db import models

# Create your models here.





class Curso(models.Model):
    nombre= models.CharField(max_length=100, unique= True)
    camada=models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Entregable (models.Model):
    nombre=models.CharField(max_length=100)
    fech_entrega=models.DateField(auto_now_add=True) #opcion para fecha actual
    entregado=models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
