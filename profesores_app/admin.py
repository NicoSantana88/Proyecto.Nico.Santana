from django.contrib import admin

# Register your models here.
from .models import Profesor, Materia

#admin.site.register(Estudiante)
@admin.register(Profesor)
class PostAdmin(admin.ModelAdmin):
    list_display=["nombre","apellido","email","materia"]
    list_filter=["apellido","materia"]
    #raw_id_fields=["autor"]
    
@admin.register(Materia)
class PostAdmin(admin.ModelAdmin):
    list_display=["nombre","turno"]
    list_filter=["nombre"]