from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class EditUserForm(UserChangeForm):
    email= forms.EmailField(required=True, label="Email")
    first_name= forms.CharField(required=True, label="Nombre")
    last_name= forms.CharField(required=True, label="Apellido")
    
    class Meta:
        model=User
        fields=("username","email","first_name", "last_name", "password" )


class MiRegistro (UserCreationForm):
    class Meta:
        model=User
        fields=("username","email","first_name", "last_name", "password1" , "password2" )
