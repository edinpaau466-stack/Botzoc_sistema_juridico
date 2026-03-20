from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Audiencia

def clientes(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        dpi = request.POST.get("dpi")
        telefono = request.POST.get("telefono")
        correo = request.POST.get("correo")
        direccion = request.POST.get("direccion")
        tipo_cliente = request.POST.get("tipo_cliente")
        estado = request.POST.get("estado")
        observaciones = request.POST.get("observaciones")

        Cliente.objects.create(
            nombre=nombre,
            dpi=dpi,
            telefono=telefono,
            correo=correo,
            direccion=direccion,
            tipo_cliente=tipo_cliente,
            estado=estado,
            observaciones=observaciones
        )

        return redirect('clientes')

    lista = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': lista})


def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('clientes')


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.nombre = request.POST.get("nombre")
        cliente.dpi = request.POST.get("dpi")
        cliente.telefono = request.POST.get("telefono")
        cliente.correo = request.POST.get("correo")
        cliente.direccion = request.POST.get("direccion")
        cliente.tipo_cliente = request.POST.get("tipo_cliente")
        cliente.estado = request.POST.get("estado")
        cliente.observaciones = request.POST.get("observaciones")
        cliente.save()

        return redirect('clientes')

    return render(request, 'clientes/editar.html', {'cliente': cliente})
from .models import Cliente, Audiencia

def audiencias(request):
    if request.method == "POST":
        cliente_id = request.POST.get("cliente")
        tipo = request.POST.get("tipo")
        proceso = request.POST.get("proceso")
        juzgado = request.POST.get("juzgado")
        fecha = request.POST.get("fecha")
        hora = request.POST.get("hora")
        descripcion = request.POST.get("descripcion")

        cliente = Cliente.objects.get(id=cliente_id)

        Audiencia.objects.create(
            cliente=cliente,
            tipo=tipo,
            proceso=proceso,
            juzgado=juzgado,
            fecha=fecha,
            hora=hora,
            descripcion=descripcion
        )

        return redirect('audiencias')

    buscar = request.GET.get("buscar")

    if buscar:
        audiencias = Audiencia.objects.filter(cliente_nombre_icontains=buscar)
    else:
        audiencias = Audiencia.objects.all()

    clientes = Cliente.objects.all()

    return render(request, 'clientes/audiencias.html', {
        'clientes': clientes,
        'audiencias': audiencias
    })

def recordatorios(request):
    return render(request, 'clientes/recordatorios.html')
def editar_audiencia(request, id):
    audiencia = get_object_or_404(Audiencia, id=id)

    if request.method == "POST":
        audiencia.tipo = request.POST.get("tipo")
        audiencia.proceso = request.POST.get("proceso")
        audiencia.juzgado = request.POST.get("juzgado")
        audiencia.fecha = request.POST.get("fecha")
        audiencia.hora = request.POST.get("hora")
        audiencia.descripcion = request.POST.get("descripcion")
        audiencia.save()
        return redirect('audiencias')

    return render(request, 'clientes/editar_audiencia.html', {'audiencia': audiencia})
def editar_audiencia(request, id):
    audiencia = get_object_or_404(Audiencia, id=id)

    if request.method == "POST":
        audiencia.tipo = request.POST.get("tipo")
        audiencia.proceso = request.POST.get("proceso")
        audiencia.juzgado = request.POST.get("juzgado")
        audiencia.fecha = request.POST.get("fecha")
        audiencia.hora = request.POST.get("hora")
        audiencia.descripcion = request.POST.get("descripcion")
        audiencia.save()
        return redirect('audiencias')

    return render(request, 'clientes/editar_audiencia.html', {'audiencia': audiencia})
