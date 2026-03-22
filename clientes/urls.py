from django.urls import path
from . import views

urlpatterns = [

    # ================= PANEL =================
    path('panel/', views.panel, name='panel'),

    # ================= EDITAR =================
    path('editar_cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('editar_audiencia/<int:id>/', views.editar_audiencia, name='editar_audiencia'),
    path('editar_expediente/<int:id>/', views.editar_expediente, name='editar_expediente'),

    # ================= ELIMINAR =================
    path('eliminar_cliente/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('eliminar_audiencia/<int:id>/', views.eliminar_audiencia, name='eliminar_audiencia'),
    path('eliminar_expediente/<int:id>/', views.eliminar_expediente, name='eliminar_expediente'),

]
