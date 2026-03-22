from django.shortcuts import render, redirect
from .models import Cliente, Audiencia, Expediente
from datetime import datetime


def panel(request):
    seccion = request.GET.get('seccion', 'clientes')

    clientes = Cliente.objects.all()
    audiencias = Audiencia.objects.all()
    expedientes = Expediente.objects.all()

    # ================= CLIENTES =================
    if seccion == 'clientes':
        if request.method == 'POST':
            Cliente.objects.create(
                nombre=request.POST.get('nombre'),
                telefono=request.POST.get('telefono'),
                dpi=request.POST.get('dpi'),
                correo=request.POST.get('correo'),
                direccion=request.POST.get('direccion'),
                tipo_caso=request.POST.get('tipo_caso'),
                fecha_nacimiento=request.POST.get('fecha_nacimiento')
            )
            return redirect('/clientes/panel/?seccion=clientes')

    # ================= AUDIENCIAS =================
    if seccion == 'audiencias':
        if request.method == 'POST':
            cliente = Cliente.objects.get(id=request.POST.get('cliente'))

            Audiencia.objects.create(
                cliente=cliente,
                fecha=request.POST.get('fecha'),
                hora=request.POST.get('hora'),
                expediente=request.POST.get('expediente'),
                tipo_caso=request.POST.get('tipo_caso'),
                dpi=request.POST.get('dpi'),
                correo=request.POST.get('correo'),
                proceso=request.POST.get('proceso'),
                juzgado=request.POST.get('juzgado'),
                estado=request.POST.get('estado'),
                observaciones=request.POST.get('observaciones')
            )
            return redirect('/clientes/panel/?seccion=audiencias')

    # ================= EXPEDIENTES =================
    if seccion == 'expedientes':
        if request.method == 'POST':
            cliente = Cliente.objects.get(id=request.POST.get('cliente'))

            Expediente.objects.create(
                cliente=cliente,
                numero=request.POST.get('numero'),
                tipo_caso=request.POST.get('tipo_caso'),
                estado=request.POST.get('estado'),
                gaveta=request.POST.get('gaveta'),
                archivo=request.POST.get('archivo')
            )
            return redirect('/clientes/panel/?seccion=expedientes')

    return render(request, 'clientes/panel.html', {
        'clientes': clientes,
        'audiencias': audiencias,
        'expedientes': expedientes,
        'seccion': seccion
    })


# ================= EDITAR CLIENTE =================
def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.telefono = request.POST.get('telefono')
        cliente.dpi = request.POST.get('dpi')
        cliente.correo = request.POST.get('correo')
        cliente.direccion = request.POST.get('direccion')
        cliente.tipo_caso = request.POST.get('tipo_caso')
        cliente.save()

        return redirect('/clientes/panel/?seccion=clientes')

    return render(request, 'clientes/editar_cliente.html', {'cliente': cliente})


# ================= ELIMINAR CLIENTE =================
def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/clientes/panel/?seccion=clientes')


# ================= EDITAR AUDIENCIA =================
def editar_audiencia(request, id):
    audiencia = Audiencia.objects.get(id=id)

    if request.method == 'POST':
        audiencia.fecha = request.POST.get('fecha')
        audiencia.hora = request.POST.get('hora')
        audiencia.expediente = request.POST.get('expediente')
        audiencia.tipo_caso = request.POST.get('tipo_caso')
        audiencia.dpi = request.POST.get('dpi')
        audiencia.correo = request.POST.get('correo')
        audiencia.proceso = request.POST.get('proceso')
        audiencia.juzgado = request.POST.get('juzgado')
        audiencia.estado = request.POST.get('estado')
        audiencia.observaciones = request.POST.get('observaciones')
        audiencia.save()

        return redirect('/clientes/panel/?seccion=audiencias')

    return render(request, 'clientes/editar_audiencia.html', {'audiencia': audiencia})


# ================= ELIMINAR AUDIENCIA =================
def eliminar_audiencia(request, id):
    audiencia = Audiencia.objects.get(id=id)
    audiencia.delete()
    return redirect('/clientes/panel/?seccion=audiencias')


# ================= EDITAR EXPEDIENTE =================
def editar_expediente(request, id):
    expediente = Expediente.objects.get(id=id)

    if request.method == 'POST':
        expediente.numero = request.POST.get('numero')
        expediente.tipo_caso = request.POST.get('tipo_caso')
        expediente.estado = request.POST.get('estado')
        expediente.gaveta = request.POST.get('gaveta')
        expediente.archivo = request.POST.get('archivo')
        expediente.save()

        return redirect('/clientes/panel/?seccion=expedientes')

    return render(request, 'clientes/editar_expediente.html', {'expediente': expediente})


# ================= ELIMINAR EXPEDIENTE =================
def eliminar_expediente(request, id):
    expediente = Expediente.objects.get(id=id)
    expediente.delete()
    return redirect('/clientes/panel/?seccion=expedientes')
