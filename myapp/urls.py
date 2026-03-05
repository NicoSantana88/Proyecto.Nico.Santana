from django.urls import path
from myapp import views_intro
from django.contrib.auth.views import LoginView
app_name="myapp"

urlpatterns = [
    path("Inicio", views_intro.indexPrueba, name="Inicio"),
    path("", views_intro.logeo, name="logeo"),
    path("perfil", views_intro.perfil, name="perfil"),
    path("editar_perfil", views_intro.editar_perfil, name="editar_perfil"),
    path("login/", LoginView.as_view(template_name="myapp/login.html"), name="login"),
]