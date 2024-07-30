from django.db import models

# Create your models here.
class Curso(models.Model):
    curso = models.CharField(max_length=20)
    camada = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class Alumnos(models.Model) :
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    
class Profesores(models.Model) :
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    