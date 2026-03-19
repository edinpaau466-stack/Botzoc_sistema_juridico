from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),
    path('audiencias/', views.audiencias, name='audiencias'),
    path('recordatorios/', views.recordatorios, name='recordatorios'),
]
