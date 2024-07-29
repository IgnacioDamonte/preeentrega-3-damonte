from django.shortcuts import render
from app.models import Curso
from django.http import HttpResponse
# Create your views here.
def inicio (request) :
    return render(request, "app/index.html")

def cursos (request) :
    return render(request, "app/cursos.html")

def alumnos (request) :
    return render(request, "app/alumnos.html")

def profesores (request) :
    return render(request, "app/profesores.html")


