from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Audiencia(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField()

    def __str__(self):
        return self.descripcion


class Recordatorio(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField()

    def __str__(self):
        return self.descripcion
