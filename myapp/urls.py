from django.urls import path
from . import views_intro

app_name="myapp"

urlpatterns = [
    path("inicio", views_intro.indexPrueba, name="Inicio"),
]