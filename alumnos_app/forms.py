from django import forms
from .models import Estudiante


class PostForm(forms.ModelForm):
    class Meta:
        model= Estudiante
        fields= ["nombre","apellido","direccion","email",]
