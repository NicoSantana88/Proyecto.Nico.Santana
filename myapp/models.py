from django.db import models

# Create your models here.







class Entregable (models.Model):
    nombre=models.CharField(max_length=100)
    fech_entrega=models.DateField(auto_now_add=True) #opcion para fecha actual
    entregado=models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
