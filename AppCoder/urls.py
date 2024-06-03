from django.urls import path
from AppCoder.views import curso, lista_cursos, inicio, cursos, profesores, estudiantes, entregable


urlpatterns = [
    path('agrega_curso/<nombre>/<camada>', curso),
    path('lista_cursos/', lista_cursos),
    path('inicio/', inicio),
    path('cursos/', cursos),
    path('estudiantes/', estudiantes),
    path('entregables/', entregable),
    path('profesores/', profesores),
     ]
