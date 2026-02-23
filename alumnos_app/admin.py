from django.contrib import admin

# Register your models here.
from .models import Estudiante

#admin.site.register(Estudiante)
@admin.register(Estudiante)
class PostAdmin(admin.ModelAdmin):
    list_display=["nombre","apellido","email","autor"]
    list_filter=["apellido","autor"]
    raw_id_fields=["autor"]
    #ordering=["nombre"] en caso que quiera ordenar por algun parametro