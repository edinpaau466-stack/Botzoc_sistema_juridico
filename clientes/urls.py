from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('audiencias/', views.audiencias, name='audiencias'),
    path('recordatorios/', views.recordatorios, name='recordatorios'),
    path('eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('eliminar_audiencia/<int:id>/', views.eliminar_audiencia, name='eliminar_audiencia'),
    path('eliminar_recordatorio/<int:id>/', views.eliminar_recordatorio, name='eliminar_recordatorio'),
]
