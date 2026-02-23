from django import forms
from .models import Profesor


class PostForm(forms.ModelForm):
    class Meta:
        model= Profesor
        fields= ["nombre","apellido","email","profesion"]
