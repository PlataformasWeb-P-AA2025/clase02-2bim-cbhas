from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

    def __str__(self):
        return "%s - %s - %s - edad: %d" % (
            self.nombre,
            self.apellido,
            self.cedula,
            self.edad
        )

class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    poblacion = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s" % (
            self.nombre,
            self.poblacion
        )
