from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name='clientes'),

    path('eliminar/<int:id>/', views.eliminar_cliente),
    path('editar/<int:id>/', views.editar_cliente),

    path('audiencias/', views.audiencias, name='audiencias'),
    path('recordatorios/', views.recordatorios, name='recordatorios'),

    path('editar_audiencia/<int:id>/', views.editar_audiencia, name='editar_audiencia'),
]
