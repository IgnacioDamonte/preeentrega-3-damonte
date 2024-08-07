from django.shortcuts import render
from .models import Curso, Alumnos, Profesores
from .forms import CursoForm, BuscarCursoForm, AlumnosForm, ProfesoresForm


# Create your views here.
def inicio (request) :
    return render(request, "app/index.html")

def cursos(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['curso']
            camada = form.cleaned_data['camada']
            curso = Curso(nombre=nombre, camada=camada)
            curso.save()
            return render(request, "app/index.html")
    else:
        form = CursoForm()

    return render(request, "app/cursos.html", {'form': form})

def buscarCursos (request):
    if request.method == 'POST':
        form = BuscarCursoForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            cursos = Curso.objects.filter(nombre=informacion['curso'])

        return render(request, "app/mostrar_cursos.html", {'cursos': cursos})
    else:
        form = BuscarCursoForm()

    return render(request, "app/buscar_cursos.html", {'form': form})

def alumnos (request) :
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            alumnos = Alumnos(nombre=nombre, apellido=apellido)
            alumnos.save()
            return render(request, "app/index.html")
    else:
        form = AlumnosForm()

    return render(request, "app/alumnos.html", {'form': form})

def buscarAlumnos (request):
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            alumnos = Alumnos.objects.filter(nombre=informacion['nombre'], apellido=informacion['apellido'])

        return render(request, "app/mostrar_alumnos.html", {'alumnos': alumnos})
    else:
        form = AlumnosForm()

    return render(request, "app/buscar_alumnos.html", {'form': form})

def profesores (request) :
    if request.method == 'POST':
        form = ProfesoresForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            profesores = Profesores(nombre=nombre, apellido=apellido, email=email)
            profesores.save()
            return render(request, "app/index.html")
    else:
        form = ProfesoresForm()

    return render(request, "app/profesores.html", {'form': form})

def buscarProfesores (request):
    if request.method == 'POST':
        form = ProfesoresForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            profesores = Profesores.objects.filter(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])

        return render(request, "app/mostrar_profesores.html", {'profesores': profesores})
    else:
        form = ProfesoresForm()

    return render(request, "app/buscar_profesores.html", {'form': form})