from django.urls import path 
from .views import mensajes

# IMPLEMENTAMOS LA VINCULACION DE URLS pnto3

app_name = 'mensajes'

urlPatterns = [
    path (
        'recibidos/', mensajes, name = 'mensaje'
    )
]