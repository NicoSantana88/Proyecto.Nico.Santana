from django.urls import path
from profesores_app import views

app_name="profesores_app"
urlpatterns = [
    path("Lista_Profesor/", views.profesor_list, name="Profesores"),
    path("new/profesor",views.post_profesor, name="Profesor_Nuevo")
]

