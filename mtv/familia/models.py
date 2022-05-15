from email.utils import format_datetime
from django.db import models

# Create your models here. 


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha = models.DateField()
    