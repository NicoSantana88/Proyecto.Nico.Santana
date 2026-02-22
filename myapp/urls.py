from django.urls import path
from myapp import views_intro

app_name="myapp"

urlpatterns = [
    path("", views_intro.indexPrueba, name="Inicio"),
]