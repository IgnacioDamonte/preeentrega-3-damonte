from django.urls import path
from app import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path('cursos/', views.cursos,name="Cursos"),
    path('buscar-cursos/', views.buscarCursos,name="BuscarCursos"),
    path('alumnos/', views.alumnos,name="Alumnos"),
    path('buscar_alumnos/',views.buscarAlumnos,name="BuscarAlumnos"),
    path('profesores/', views.profesores,name="Profesores"),
    path('buscar_profesores/', views.buscarProfesores,name="BuscarProfesores")
    #path('curso-formulario/', views.curso_formulario, name="CursoFormulario"),
    #path('form-con-api/', views.form_con_api, name="FormConApi"),
    #path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),


]
