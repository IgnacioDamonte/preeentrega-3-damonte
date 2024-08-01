from django import forms

class CursoForm(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class BuscarCursoForm(forms.Form):
    curso = forms.CharField()

class AlumnosForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    
class BuscarAlumnos(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    
    

class Profesores(forms.Form):
    nombre = forms.CharField()
    apellido = forms.IntegerField()
    email = forms.EmailField()
    
class ProfesoresForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
