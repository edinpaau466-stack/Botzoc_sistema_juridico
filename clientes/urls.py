from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('audiencias/', views.audiencias, name='audiencias'),
    path('recordatorios/', views.recordatorios, name='recordatorios'),
]
path('', views.inicio, name='inicio'),
