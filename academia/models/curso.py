from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cupo = models.IntegerField()

    def __str__(self):
        return self.nombre