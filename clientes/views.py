from django.shortcuts import render, redirect
from .models import Cliente

def clientes(request):
    lista = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': lista})

def audiencias(request):
    return render(request, 'audiencias.html')

def recordatorios(request):
    return render(request, 'recordatorios.html')
