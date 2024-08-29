from django.shortcuts import render
from .models import Mensaje

# Create your views here.
# IMPLEMENTACION DE LA VISTA punto3

def mensajes (request):
    recibidos = Mensaje.objects.all

    return render(request,'mensajes/Mensajes.html', {'mensajes':recibidos}) 