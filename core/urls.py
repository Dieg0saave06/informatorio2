from django.urls import path
from core import views

urlpatterns = [
    path("index/", views.indexView, name = "index"),
    path("publicaciones/", views.publicacionesView, name = "publicaciones"),
    path("perfil/", views.perfilView, name = "perfil"),
    path("ajustes", views.ajustesView, name = "ajustes"),
    path("cerrar_sesion/", views.sesionView, name = "cerrar_sesion")
]