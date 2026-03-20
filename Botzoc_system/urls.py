from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def inicio(request):
    return redirect('/clientes/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),  # redirige al inicio
    path('clientes/', include('clientes.urls')),
]
