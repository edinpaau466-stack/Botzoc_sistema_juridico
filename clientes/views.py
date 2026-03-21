from django.shortcuts import render, redirect
from .models import Cliente, Audiencia
from datetime import date, timedelta

# =========================
# HOME (Pantalla principal)
# =========================
def home(request):
    return render(request, 'clientes/home.html')


# =========================
# PANEL PRINCIPAL
# =========================
def panel(request):
    seccion = request.GET.get('seccion', 'clientes')

    clientes = Cliente.objects.all()
    audiencias = Audiencia.objects.all()

    manana = date.today() + timedelta(days=1)
    recordatorios = Audiencia.objects.filter(fecha=manana)

    context = {
        'seccion': seccion,
        'clientes': clientes,
        'audiencias': audiencias,
        'recordatorios': recordatorios
    }

    return render(request, 'clientes/panel.html', context)


# =========================
# CLIENTES
# =========================
def clientes(request):
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST['nombre'],
            dpi=request.POST['dpi'],
            telefono=request.POST['telefono'],
            correo=request.POST['correo'],
            direccion=request.POST['direccion'],
            tipo_cliente=request.POST['tipo_cliente'],
            estado=request.POST['estado'],
            observaciones=request.POST['observaciones']
        )
        return redirect('/clientes/panel/?seccion=clientes')

    return render(request, 'clientes/clientes.html', {'clientes': clientes})


def eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/clientes/panel/?seccion=clientes')


def editar(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.dpi = request.POST['dpi']
        cliente.telefono = request.POST['telefono']
        cliente.correo = request.POST['correo']
        cliente.direccion = request.POST['direccion']
        cliente.tipo_cliente = request.POST['tipo_cliente']
        cliente.estado = request.POST['estado']
        cliente.observaciones = request.POST['observaciones']
        cliente.save()

        return redirect('/clientes/panel/?seccion=clientes')

    return render(request, 'clientes/editar.html', {'cliente': cliente})


# =========================
# AUDIENCIAS
# =========================
def audiencias(request):
    clientes = Cliente.objects.all()
    audiencias = Audiencia.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        cliente = Cliente.objects.get(id=cliente_id)

        Audiencia.objects.create(
            cliente=cliente,
            tipo=request.POST['tipo'],
            proceso=request.POST['proceso'],
            juzgado=request.POST['juzgado'],
            fecha=request.POST['fecha'],
            hora=request.POST['hora'],
            descripcion=request.POST['descripcion']
        )

        return redirect('/clientes/panel/?seccion=audiencias')

    return render(request, 'clientes/audiencias.html', {
        'clientes': clientes,
        'audiencias': audiencias
    })


def eliminar_audiencia(request, id):
    audiencia = Audiencia.objects.get(id=id)
    audiencia.delete()
    return redirect('/clientes/panel/?seccion=audiencias')


# =========================
# RECORDATORIOS
# =========================
def recordatorios(request):
    manana = date.today() + timedelta(days=1)
    audiencias = Audiencia.objects.filter(fecha=manana)

    return render(request, 'clientes/recordatorios.html', {
        'audiencias': audiencias
    })
