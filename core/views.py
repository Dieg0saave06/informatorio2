from django.shortcuts import render
from core.models import Publicaciones
# Create your views here.
def indexView(request):
    return render(request, "index.html", {})

def publicacionesView(request):
    ctx = {
        "posteos" : Publicaciones.objects.all()
    }
    return render(request, "publicaciones.html", ctx)

def perfilView(request):
    return render(request, "perfil.html", {})

def ajustesView(request):
    return render(request, "ajustes.html", {})

def sesionView(request):
    return render(request, "cerrar_sesion.html", {})
    
