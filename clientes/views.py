from django.shortcuts import render, redirect
from .models import Cliente, Audiencia, Expediente, Recordatorio

# ========================
# CLIENTES
# ========================
def clientes(request):
    lista_clientes = Cliente.objects.all()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        proceso = request.POST.get('proceso')

        Cliente.objects.create(
            nombre=nombre,
            telefono=telefono,
            correo=correo,
            proceso=proceso
        )

        return redirect('clientes')

    return render(request, 'clientes.html', {
        'clientes': lista_clientes
    })


def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes')


# ========================
# AUDIENCIAS
# ========================
def audiencias(request):
    busqueda = request.GET.get('buscar')

    if busqueda:
        lista = Audiencia.objects.filter(juzgado__icontains=busqueda)
    else:
        lista = Audiencia.objects.all()

    if request.method == 'POST':
        expediente_id = request.POST.get('expediente')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        juzgado = request.POST.get('juzgado')
        tipo = request.POST.get('tipo')

        expediente = Expediente.objects.get(id=expediente_id)

        Audiencia.objects.create(
            expediente=expediente,
            fecha=fecha,
            hora=hora,
            juzgado=juzgado,
            tipo_audiencia=tipo
        )

        return redirect('audiencias')

    expedientes = Expediente.objects.all()

    return render(request, 'audiencias.html', {
        'audiencias': lista,
        'expedientes': expedientes
    })


def eliminar_audiencia(request, id):
    audiencia = Audiencia.objects.get(id=id)
    audiencia.delete()
    return redirect('audiencias')


# ========================
# RECORDATORIOS
# ========================
def recordatorios(request):
    busqueda = request.GET.get('buscar')

    if busqueda:
        lista = Recordatorio.objects.filter(descripcion__icontains=busqueda)
    else:
        lista = Recordatorio.objects.all()

    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')

        Recordatorio.objects.create(
            descripcion=descripcion,
            fecha=fecha
        )

        return redirect('recordatorios')

    return render(request, 'recordatorios.html', {
        'recordatorios': lista
    })


def eliminar_recordatorio(request, id):
    recordatorio = Recordatorio.objects.get(id=id)
    recordatorio.delete()
    return redirect('recordatorios')
