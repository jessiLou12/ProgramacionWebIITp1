from django.shortcuts import render
from .models import Mensajes

# Create your views here.
# IMPLEMENTACION DE LA VISTA punto3

def mensaje (request):
    recibidos = Mensajes.objects.all

    return render(request,'mensaje/Mensajes.html', {'mensaje':recibidos}) 