from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    proceso = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nombre


class Expediente(models.Model):
    numero_expediente = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_proceso = models.CharField(max_length=200)
    juzgado = models.CharField(max_length=200)
    estado = models.CharField(max_length=100)

    def _str_(self):
        return self.numero_expediente


class Audiencia(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    juzgado = models.CharField(max_length=200)
    tipo_audiencia = models.CharField(max_length=200)

    def _str_(self):
        return f"{self.expediente} - {self.fecha}"


class Recordatorio(models.Model):
    audiencia = models.ForeignKey(Audiencia, on_delete=models.CASCADE)
    horas_antes = models.IntegerField()
    enviado = models.BooleanField(default=False)

    def _str_(self):
        return f"Recordatorio {self.horas_antes}h antes"
