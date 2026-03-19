from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),
    path('eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('audiencias/', views.audiencias, name='audiencias'),
    path('eliminar_audiencia/<int:id>/', views.eliminar_audiencia, name='eliminar_audiencia'),
    path('recordatorios/', views.recordatorios, name='recordatorios'),
    path('eliminar_recordatorio/<int:id>/', views.eliminar_recordatorio, name='eliminar_recordatorio'),
]
