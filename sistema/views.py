from django.shortcuts import render
from .utils import obtener_datos_sistema

def home(request):
    datos = obtener_datos_sistema()
    return render(request, "sistema/index.html", {"datos": datos})
