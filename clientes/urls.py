from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel, name='panel'),

    path('audiencias/', views.audiencias, name='audiencias'),
    path('recordatorios/', views.recordatorios, name='recordatorios'),
]
