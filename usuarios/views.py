from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import RegistrarseForm
from django.urls import reverse

# Create your views here.

# VISTA BASADA EN CLASE QUE CREA UN USUARIO
class RegistroView(CreateView):
    model = Usuario
    template_name = "usuarios/registro.html"
    form_class = RegistrarseForm

    def get_success_url(self):
        return reverse("index")