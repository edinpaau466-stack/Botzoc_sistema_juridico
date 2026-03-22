from django.db import models

class Ley(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='leyes/')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
from django.db import models

class Ley(models.Model):
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='leyes/')
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
