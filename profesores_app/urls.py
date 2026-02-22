from django.urls import path
from . import views

app_name="profesores_app"
urlpatterns = [
    path("Profesores", views, name="Profesores"),
]

