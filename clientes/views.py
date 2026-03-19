from django.shortcuts import render, redirect
from .models import Cliente

def clientes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')

        Cliente.objects.create(
            nombre=nombre,
            direccion=direccion
        )

        return redirect('clientes')

    lista = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': lista})


def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes')
