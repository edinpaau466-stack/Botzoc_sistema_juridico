from django.contrib import admin
from .models import Cliente, Expediente, Audiencia, Recordatorio


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)


@admin.register(Expediente)
class ExpedienteAdmin(admin.ModelAdmin):
    autocomplete_fields = ["cliente"]
    search_fields = ("numero_expediente",)
    list_display = ("numero_expediente", "cliente", "tipo_proceso", "juzgado", "estado")


@admin.register(Audiencia)
class AudienciaAdmin(admin.ModelAdmin):
    list_display = ("expediente", "fecha", "hora", "juzgado", "tipo_audiencia")
    list_filter = ("fecha", "juzgado")
    search_fields = ("expediente__numero_expediente",)
    autocomplete_fields = ["expediente"]
    ordering = ("fecha", "hora")

@admin.register(Recordatorio)
class RecordatorioAdmin(admin.ModelAdmin):
    list_display = ("audiencia", "horas_antes", "enviado")
    list_filter = ("enviado",)
