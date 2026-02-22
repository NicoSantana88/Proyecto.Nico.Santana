from django.urls import path
from profesores_app import views

app_name="profesores_app"
urlpatterns = [
    path("Profesores", views.profesor_list, name="Profesores"),
]

