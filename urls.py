from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),
]
from django.shortcuts import render

def home(request):
    return render(request, 'bufete.html')
