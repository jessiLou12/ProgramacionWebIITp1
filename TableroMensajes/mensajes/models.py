from django.db import models
from django.utils import timezone



# Create your models here.
# DESARROLLO DE MODELO pnto2

class Mensaje (models.Model):
    texto = models.TextField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField(default=timezone.now)