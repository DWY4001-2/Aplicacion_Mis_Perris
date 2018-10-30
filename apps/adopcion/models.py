from django.db import models

# Create your models here.

class Persona(models.Model):
	email = models.EmailField()
	run = models.CharField(max_length=10)
	nombre = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	telefono = models.CharField(max_length=12)
	region = models.TextField()
	ciudad = models.TextField()
	vivienda = models.TextField()
