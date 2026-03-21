from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'bufete.html')

urlpatterns = [
    path('', home),
    path('clientes/', include('clientes.urls')),
    path('admin/', admin.site.urls),
]
