from django.shortcuts import render, redirect
from .models import Cliente

def clientes(request):
    seccion = request.GET.get('seccion', 'clientes')

    clientes = Cliente.objects.all()

    return render(request, 'clientes/clientes.html', {
        'clientes': clientes,
        'seccion': seccion
    })
