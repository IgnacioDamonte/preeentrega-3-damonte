from django import forms

class Curso(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class Alumnos(forms.Form):
    nombre = forms.CharField()
    apellido = forms.IntegerField()

class Profesores(forms.Form):
    nombre = forms.CharField()
    apellido = forms.IntegerField()
    email = forms.EmailField()
