from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    dpi = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.TextField()
    tipo_caso = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre


class Audiencia(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField(null=True, blank=True)

    expediente = models.CharField(max_length=100, null=True, blank=True)
    tipo_caso = models.CharField(max_length=100, null=True, blank=True)
    dpi = models.CharField(max_length=20, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    proceso = models.CharField(max_length=100, null=True, blank=True)
    juzgado = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=50, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.cliente.nombre} - {self.fecha}"


class Expediente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=100)
    tipo_caso = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    gaveta = models.CharField(max_length=50)
    archivo = models.CharField(max_length=50)

    def __str__(self):
        return self.numero
