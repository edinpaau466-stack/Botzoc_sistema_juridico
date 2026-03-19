from django.contrib import admin
from .models import Cliente, Expediente, Audiencia, Recordatorio

admin.site.register(Cliente)
admin.site.register(Expediente)
admin.site.register(Audiencia)
admin.site.register(Recordatorio)
