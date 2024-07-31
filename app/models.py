from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()

    def str(self):
        return f"{self.nombre} - {self.camada}"

class Alumnos(models.Model) :
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    
    def str(self):
        return f"{self.nombre} - {self.apellido}"
    

class Profesores(models.Model) :
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40) 
