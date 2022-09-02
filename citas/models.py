from random import choices
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Consultorio(models.Model):
    numero = models.IntegerField()
    class Meta:
        verbose_name ='consultorio'
        verbose_name_plural ='consultorios'
    def __str__(self):
        return self.numero
class Horario(models.Model):
    turno = models.DateTimeField()
class Medico(models.Model):
    nombre = models.CharField(max_length=50)    
    apellido = models.CharField(max_length=50)
    especializacion = models.CharField(max_length=100)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.SET_NULL,blank=True, null=True,)
    turno = models.ForeignKey(Horario, on_delete=models.SET_NULL,blank=True, null=True,)
    class Meta:
        verbose_name ='medico'
        verbose_name_plural ='medicos'
    def __str__(self):
        return self.nombre
    
class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL,blank=True, null=True,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name ='servicio'
        verbose_name_plural ='servicios'
    def __str__(self):
        return self.titulo
class Cita(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
