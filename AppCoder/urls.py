from django.urls import path
from AppCoder.views import (curso, 
lista_cursos, 
inicio, cursos, 
profesores, 
estudiantes, 
entregable,
curso_formulario,
busqueda_camada, 
buscar

)

urlpatterns = [
    path('agrega_curso/<nombre>/<camada>', curso),
    path('lista_cursos/', lista_cursos),
    path('inicio/', inicio, name='Inicio'),
    path('cursos/', cursos, name='Cursos'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregable, name='Entregables'),
    path('profesores/', profesores, name='Profesores'),
    path('curso-formulario/', curso_formulario, name='CursoFormulario'),
    path('busqueda-camada/', busqueda_camada, name='BusquedaCamada'),
    path('buscar/', buscar, name='BuscarCurso'),

    ]
