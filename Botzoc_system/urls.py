from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# REDIRECCIÓN AUTOMÁTICA AL SISTEMA
def inicio(request):
    return redirect('/clientes/')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página principal → redirige al sistema
    path('', inicio),

    # Sistema principal
    path('clientes/', include('clientes.urls')),
]
