from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request, "index.html", {})

def perfilView(request):
    return render(request, "perfil.html", {})

def ajustesView(request):
    return render(request, "ajustes.html", {})

def sesionView(request):
    return render(request, "cerrar_sesion.html", {})
    
