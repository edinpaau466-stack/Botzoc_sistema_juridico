from django.urls import path
from .views import home, clientes_view, audiencias_view, recordatorios_view

urlpatterns = [
    path('', home),
    path('clientes/', clientes_view),
    path('audiencias/', audiencias_view),
    path('recordatorios/', recordatorios_view),
]
