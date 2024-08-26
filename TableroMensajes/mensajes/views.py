from django.shortcuts import render
from .models import Mensajes

# Create your views here.
# IMPLEMENTACION DE LA VISTA punto3

def mensajes (request):
    recibidos = Mensajes.objects.all

    return render(request,'mensajes,mensajes.html', {'mensjaes':recibidos}) 