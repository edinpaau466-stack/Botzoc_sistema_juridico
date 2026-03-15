from django.db import models

 
class Cliente(models.Model):

    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    dpi = models.CharField(max_length=20)
    direccion = models.CharField(max_length=300)
    proceso = models.CharField(max_length=200)
    juzgado = models.CharField(max_length=200)
    fecha_audiencia = models.DateTimeField()
    estado= models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre

def __str__(self):
    return self.nombre


class Expediente(models.Model):
    numero_expediente = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_proceso = models.CharField(max_length=200)
    juzgado = models.CharField(max_length=200)
    estado = models.CharField(max_length=100)
    fecha_inicio = models.DateField()

    def __str__(self):
        return self.numero_expediente


class Audiencia(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    juzgado = models.CharField(max_length=200)
    tipo_audiencia = models.CharField(max_length=200)
    observaciones = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        tiempos = [24, 5, 3, 1]

        for horas in tiempos:
            Recordatorio.objects.get_or_create(
                audiencia=self,
                horas_antes=horas
            )

    def __str__(self):
        return f"{self.expediente} - {self.fecha}"

    def __str__(self):
        return f"{self.expediente} - {self.fecha}"

    def __str__(self):
        return f"{self.expediente} - {self.fecha}"


class Recordatorio(models.Model):
    audiencia = models.ForeignKey(Audiencia, on_delete=models.CASCADE)
    horas_antes = models.IntegerField()
    enviado = models.BooleanField(default=False)

    def __str__(self):
        return f"Recordatorio {self.horas_antes}h antes - {self.audiencia}"


def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    tiempos = [24, 5, 3, 1]

    for horas in tiempos:
        Recordatorio.objects.get_or_create(
            audiencia=self,
            horas_antes=horas
        )
