from django.http import HttpResponse
from django.shortcuts import render
from.models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# Create your views here.

def curso(req, nombre, camada):

    nuevo_curso = Curso(nombre=nombre, camada=camada)
    nuevo_curso.save()

    return  HttpResponse(f"""
    <p>Curso: {nuevo_curso.nombre} - Camada: {nuevo_curso.camada} creado!</p>
""")

def lista_cursos(req):

    lista = Curso.objects.all()

    return render(req, "lista_cursos.html", {"lista_cursos": lista})

def inicio(req):

    return render(req, "inicio.html", {})

def cursos(req):

    return render(req, "cursos.html", {})

def profesores(req):

    return render(req, "profesores.html", {})

def estudiantes(req):

    return render(req, "estudiantes.html", {})

def entregable(req):

    return render(req, "entregables.html", {})

def curso_formulario(req):
    
    print('method: ', req.method)
    print('POST: ', req.POST)
    
    if req.method == 'POST':
        
        miFormulario = CursoFormulario(req.POST)
        
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
         
            nuevo_curso = Curso(nombre=req.POST['curso'], camada=req.POST['camada'])
            nuevo_curso.save()
        
            return render(req, "inicio.html", {"message": "Curso creado con exito"})
    
        else:
        
            return render(req, "inicio.html", {"message": "Datos invalidos"})
        
    else:
        
        miFormulario = CursoFormulario
        
        return render(req, "curso_formulario.html", {"miFormulario": miFormulario})
    
def busqueda_camada(req):
    
    return render(req, "busqueda_camada.html", {}) 

def buscar(req):
    
    if req.GET["camada"]:
        
        camada = req.GET["camada"]
        
        cursos = Curso.objects.filter(camada=camada)
          
        return render(req,"resultadoBusqueda.html", {"cursos": cursos, "camada": camada} )
    
    else:
        
        return render(req,"inicio.html", {"message": "No enviaste el dato de la camada"} )
    
    
def lista_profesores(req):
    
    mis_profesores = Profesor.objects.all()
    
    return render(req,"leer_profesores.html", {"profesores": mis_profesores} )



def crea_profesor(req,):
    
    if req.method == 'POST':
        
        miFormulario = ProfesorFormulario(req.POST)
        
        if miFormulario.is_valid():
            
          data = miFormulario.cleaned_data
         
          nuevo_profesor = Profesor(nombre=req.POST['nombre'], apellido=req.POST['apellido'], email=req.POST['email'], profesion=req.POST['profesion'])
          nuevo_profesor.save()
        
          return render(req, "inicio.html", {"message": "Profesor creado con exito"})
    
        else:
        
            return render(req, "inicio.html", {"message": "Datos invalidos"})
        
    else:
        
      miFormulario = ProfesorFormulario()
        
      return render(req, "profesor_formulario.html", {"miFormulario": miFormulario})
    
    
    
    
def eliminar_profesor(req, id):
    
    if req.method == 'POST':
    
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
    
    mis_profesores = Profesor.objects.all()
    return render(req,"leer_profesores.html", {"profesores": mis_profesores} )

def editar_profesor(req, id):
    
    if req.method == 'POST':
        
        miFormulario = ProfesorFormulario(req.POST)
        
        if miFormulario.is_valid():
            
          data = miFormulario.cleaned_data
          profesor = Profesor.objects.get(id=id)
          
          profesor.nombre = data["nombre"]
          profesor.apellido = data["apellido"]
          profesor.email = data["email"]
          profesor.profesion = data["profesion"]
          
          profesor.save()
         
          return render(req, "inicio.html", {"message": "Profesor actualizado con exito"})
    
        else:
        
            return render(req, "inicio.html", {"message": "Datos invalidos"})
        
    else:
        
        profesor = Profesor.objects.get(id=id)
        
        miFormulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre,
            "apellido": profesor.apellido,
            "email": profesor.email,
            "profesion": profesor.profesion,
        })
        
        return render(req, "editar_profesor.html", {"miFormulario": miFormulario, "id": profesor.id })
    
    
class CursoList(ListView):
    
    model = Curso
    template_name = 'curso_list.hmtl'
    context_object_name = "cursos"
    
    
class CursoDetail(DetailView):
    
    model = Curso
    template_name = 'curso_detail.html' 
    context_object_name = "curso"
    
class CursoCreate(CreateView):
    
    model = Curso
    template_name = 'curso_create.hmtl'
    fields = ["nombre", "camada"]
    success_url = "/app-coder/inicio/"
    
class CursoUpdate(UpdateView):
    
    model = Curso
    template_name = 'curso_update.html'
    fields = ('__all__')
    success_url = "/app-coder/inicio/"
    context_object_name = "curso"
    
class CursoDelete(DeleteView):
    
    model = Curso
    template_name = 'curso_delete.html'
    success_url = "/app-coder/inicio/"


  
    
    
    
    
    
    