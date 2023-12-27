from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    ap = models.CharField(max_length=20)
    dni = models.IntegerField()
    def __str__(self) -> str:
        return f'NOMBRE: {self.nombre} | APELLIDO: {self.ap} | DNI: {self.dni}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    ap = models.CharField(max_length=20)
    dni = models.IntegerField()
    sueldo = models.IntegerField()
    def __str__(self) -> str:
        return f'NOMBRE: {self.nombre} {self.ap} | DNI: {self.dni} | SUELDO: {self.sueldo}'

class Directivo(models.Model):
    nombre = models.CharField(max_length=20)
    ap = models.CharField(max_length=20)
    dni = models.IntegerField()
    adhonoren = models.BooleanField()
    sueldo = models.IntegerField()
    def __str__(self) -> str:
        return f'NOMBRE: {self.nombre} {self.ap} | DNI: {self.dni} | ADHONOREN: {self.adhonoren} | SUELDO: {self.sueldo}'
    

