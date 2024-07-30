from django.shortcuts import render
from app.models import Curso,Alumnos,Profesores
from app.forms import Curso

# Create your views here.
def inicio (request) :
    return render(request, "app/index.html")

def cursos (request) :
    if request.method == 'POST':
        #print(request.POST)
        #print("\n\n")
        curso = Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()

        return render(request, "app/index.html")

    return render(request,"app/cursos.html")

def alumnos (request) :
    if request.method == 'POST':
        #print(request.POST)
        #print("\n\n")
        curso = Curso(nombre=request.POST['nombre'],camada=request.POST['apellido'])
        curso.save()

        return render(request, "app/index.html")

    return render(request,"app/alumnos.html")

def profesores (request) :
    return render(request, "app/profesores.html")





#def form_con_api(request):
    if request.method == "POST":

        mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "app/index.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "app/form_con_api.html", {"mi_formulario": mi_formulario})

#from app.forms import BuscaCursoForm

#def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "app/mostrar_cursos.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "app/buscar_form_con_api.html", {"mi_formulario": mi_formulario})

