from django.shortcuts import render, redirect
from .models import Cliente

# LISTAR CLIENTES
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})

# CREAR CLIENTE
def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        Cliente.objects.create(nombre=nombre, telefono=telefono, correo=correo)
        return redirect('clientes')
    return render(request, 'clientes/crear.html')

# ELIMINAR CLIENTE
def eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes')

# EDITAR CLIENTE
def editar(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.telefono = request.POST['telefono']
        cliente.correo = request.POST['correo']
        cliente.save()
        return redirect('clientes')
    return render(request, 'clientes/editar.html', {'cliente': cliente})

# AUDIENCIAS
def audiencias(request):
    return render(request, 'clientes/audiencias.html')

# RECORDATORIOS
def recordatorios(request):
    return render(request, 'clientes/recordatorios.html')
