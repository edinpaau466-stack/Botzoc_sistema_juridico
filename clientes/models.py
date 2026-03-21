from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    dpi = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    tipo_cliente = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Audiencia(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    proceso = models.CharField(max_length=200)
    juzgado = models.CharField(max_length=200)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.cliente.nombre} - {self.tipo} - {self.fecha}"
class Expediente(models.Model):
    numero = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_caso = models.CharField(max_length=100)
    juzgado = models.CharField(max_length=100)
    proceso = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return self.numero
