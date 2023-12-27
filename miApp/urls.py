from django.urls import path
from miApp.views import (cargar_profesor,cargar_alumno,cargar_directivo,
                         ver_directivo,ver_profesor,ver_alumno,
                         index,
                         buscar_alumno)
from miApp import views


urlpatterns = [
    path('profesores/',views.ver_profesor, name='Profesor'),
    path('alumnos/',views.ver_alumno,name='Alumno'), ##
    path('directivos/',views.ver_directivo, name='Directivo'),
    path('cargarAlumno/', views.cargar_alumno, name='CargaAlumno'), 
    path('cargarProfesor/',views.cargar_profesor,name='CargaProfesor'), 
    path('cargarDirectivo/', views.cargar_directivo,name='CargaDirectivo'),
    path("", views.index, name='Inicio'),
    path('buscarAlumno',views.buscar_alumno, name='buscarAlumno')##
]
