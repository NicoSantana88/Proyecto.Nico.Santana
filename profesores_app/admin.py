from django.contrib import admin

# Register your models here.
from .models import Profesor

#admin.site.register(Estudiante)
@admin.register(Profesor)
class PostAdmin(admin.ModelAdmin):
    list_display=["nombre","apellido","email","profesion"]
    list_filter=["apellido","profesion"]
    #raw_id_fields=["autor"]