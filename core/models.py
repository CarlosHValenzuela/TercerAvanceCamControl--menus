from django.db import models # type: ignore
from .choices import tipos

class VehiclePlate(models.Model):
    plate = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    dirrecion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.plate} - {self.nombre}"
    
class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    auto_increment = True
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100,choices=tipos,default='R')
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Auto(models.Model):
    id_auto = models.AutoField(primary_key=True)
    auto_increment = True
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.placa} {self.persona}"
    