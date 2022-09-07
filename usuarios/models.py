from django.db import models
from random import choices
from tkinter import CASCADE
from citas.models import *
from django.contrib.auth.models import User


# Create your models here.
class Historial(models.Model):
    descripcion = models.TextField()
    CitasID = models.ForeignKey(Cita, on_delete=models.SET_NULL,blank=True, null=True,)
    
    class Meta:
        verbose_name = "historial"
        verbose_name_plural = "historiales"
    def _str_(self):
        return self.descripcion

class Paciente(models.Model):
    user = models.OneToOneField(User , on_delete=models.SET_NULL,blank=True, null=True)
    nombre = models.CharField( max_length=100, verbose_name ="Nombre")
    apellido = models.CharField( max_length=100, verbose_name = "Apellidos")
    cedula = models.IntegerField(verbose_name = "Documento de Identidad")
    telefono = models.CharField( max_length=70, verbose_name = "Telefono")
    fechaNac = models.DateTimeField(verbose_name = "Fecha de Nacimiento")
    direccion = models.CharField( max_length=150, verbose_name = "Dirección")
    historialid = models.ForeignKey(Historial ,on_delete=models.SET_NULL,blank=True, null=True,)
    Doctorid = models.ForeignKey(Medico, on_delete=models.SET_NULL,blank=True, null=True,)

    def nombre_completo(self):
        return "{}, {}, {}",format(self.nombre, self.apellido, self.cedula) 

    def _str_(self):
        return self.nombre_completo()
    
        class Meta:
            verbose_name = "paciente"
        verbose_name_plural = "pacientes"


class Rol(models.Model):
    tipo = models.CharField(max_length=50)
    
    
class Usuario(models.Model):
    user = models.OneToOneField(User , on_delete=models.SET_NULL,blank=True, null=True)
    nombre = models.CharField( max_length=100, verbose_name = "Nombre")
    apellido = models.CharField( max_length=100, verbose_name = "Apellidos")
    cedula = models.IntegerField(verbose_name = "Documento de Identidad")
    telefono = models.CharField( max_length=70, verbose_name = "Telefono")
    email = models.CharField( max_length=250, verbose_name = "Correo Electronico")
    direccion = models.CharField( max_length=150, verbose_name = "Dirección")
    Rolid = models.ForeignKey(Rol ,on_delete=models.SET_NULL,blank=True, null=True,)
    
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
    def __str__(self):
        return self.nombre
    

