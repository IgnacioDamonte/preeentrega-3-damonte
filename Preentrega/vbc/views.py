from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from app.models import Alumnos

class AlumnosListView(ListView) :
    model = Alumnos
    constext_object_name = "Alumnos"
    template_name = "vbc/lista_alumnos.html"
    

class AlumnosDeleteView(DeleteView) :
    model = Alumnos
    template_name = "vbc/alumnos_borrar.html"
    success_url = reverse_lazy("AlumnosBorrar")
    
class AlumnosUpdateView(UpdateView) :
    model = Alumnos
    template_name = "vbc/alumnos_actualizados.html"
    success_url = reverse_lazy("ListarAlumnos")
    fields = ["nombre" ,"apellido"]