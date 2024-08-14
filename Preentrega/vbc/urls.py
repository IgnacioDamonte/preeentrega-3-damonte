
from django.urls import path, include
from vbc import views
urlpatterns = [
    path('alumnos/listar', views.AlumnosListView.as_view(), name="ListarAlumnos"),
    path('alumnos/<pk>', views.AlumnosDeleteView.as_view(), name="BorrarAlumnos"),
    path('alumnos/<pk>/actualizar', views.AlumnosUpdateView.as_view(), name="ActualizarAlumnos"),
]
