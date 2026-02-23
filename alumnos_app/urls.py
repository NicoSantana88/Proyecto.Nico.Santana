from django.urls import path
from alumnos_app import views

app_name="alumnos_app"

urlpatterns = [
    path("Alumnos", views.estudiantes_list, name="estudiantes"),
    path("Post/Alumnos",views.post_create, name="new_alumno")
]