from django.db import models


class Materia(models.Model):
    nombre= models.CharField(max_length=100, unique= True)
    turno=models.IntegerField()
    
    def __str__(self):
        return self.nombre


# Create your models here.
class Profesor(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email =models.EmailField()
    materia= models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True, blank=True,verbose_name="materia")
    turno=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.materia}"
    
    class Meta:
        verbose_name="Profesor"
        verbose_name_plural="Profesores"
        constraints=[
            models.UniqueConstraint(fields=["materia","email"], name="materia_email")
        ]
        indexes= [models.Index(fields=["apellido", "materia"])]