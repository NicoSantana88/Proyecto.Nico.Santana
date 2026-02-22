from django.urls import path
from alumnos_app import views

app_name="alumnos_app"

urlpatterns = [
    path("Alumnos", views.estudiantes_list, name="estudiantes"),
]