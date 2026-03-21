from django.shortcuts import render, redirect
from .models import Cliente, Audiencia
from datetime import date, timedelta

# =========================
# CLIENTES
# =========================
def clientes(request):
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        nombre = request.POST['nombre']
        dpi = request.POST['dpi']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        direccion = request.POST['direccion']
        tipo_cliente = request.POST['tipo_cliente']
        estado = request.POST['estado']
        observaciones = request.POST['observaciones']

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

    return render(request, 'clientes/clientes.html', {
        'clientes': clientes
    })


def eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes')


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

        return redirect('clientes')

    return render(request, 'clientes/editar.html', {
        'cliente': cliente
    })


# =========================
# AUDIENCIAS
# =========================
def audiencias(request):
    clientes = Cliente.objects.all()
    audiencias = Audiencia.objects.all()

    if request.method == "POST":
        cliente_id = request.POST['cliente']
        tipo = request.POST['tipo']
        proceso = request.POST['proceso']
        juzgado = request.POST['juzgado']
        fecha = request.POST['fecha']
        hora = request.POST['hora']
        descripcion = request.POST['descripcion']

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

    return render(request, 'clientes/audiencias.html', {
        'clientes': clientes,
        'audiencias': audiencias
    })


# =========================
# RECORDATORIOS
# =========================
def recordatorios(request):
    mañana = date.today() + timedelta(days=1)

    audiencias = Audiencia.objects.filter(fecha=mañana)

    return render(request, 'clientes/recordatorios.html', {
        'audiencias': audiencias
    })


# =========================
# INICIO
# =========================
def inicio(request):
    return redirect('clientes')
def editar_audiencia(request, id):
    return redirect('audiencias')
from .models import Audiencia

def eliminar_audiencia(request, id):
    audiencia = Audiencia.objects.get(id=id)
    audiencia.delete()
    return redirect('audiencias')
from django.shortcuts import render

def home(request):
    return render(request, 'clientes/home.html')

def panel(request):
    seccion = request.GET.get('seccion', 'clientes')
    return render(request, 'clientes/panel.html', {
        'seccion': seccion
    })
def audiencias(request):
    return render(request, 'clientes/audiencias.html')

def recordatorios(request):
    return render(request, 'clientes/recordatorios.html')
