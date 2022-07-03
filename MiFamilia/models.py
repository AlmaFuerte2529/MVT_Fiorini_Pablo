from django.db import models

# Create your models here.


class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField()
    edad = models.IntegerField()