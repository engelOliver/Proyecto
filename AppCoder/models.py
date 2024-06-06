from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - {self.camada}"

class Estudiantes(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
 
class Profesor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)  
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField(max_length=30)
    entregado = models.BooleanField()
    

