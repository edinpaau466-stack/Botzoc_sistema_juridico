from django.shortcuts import render, redirect
from .models import Cliente, Audiencia, Expediente
from datetime import datetime


def panel(request):
    seccion = request.GET.get('seccion', 'clientes')

    # ==================== CLIENTES ====================
    if seccion == 'clientes':
        if request.method == 'POST':

            fecha_input = request.POST.get('fecha_nacimiento')
            fecha_nacimiento = None

            if fecha_input:
                try:
                    # FORMATO GUATEMALA (día/mes/año)
                    fecha_nacimiento = datetime.strptime(fecha_input, "%d/%m/%Y").date()
                except Exception:
                    try:
                        # FORMATO ISO (año-mes-día)
                        fecha_nacimiento = datetime.strptime(fecha_input, "%Y-%m-%d").date()
                    except Exception:
                        fecha_nacimiento = None

            Cliente.objects.create(
                nombre=request.POST.get('nombre'),
                telefono=request.POST.get('telefono'),
                dpi=request.POST.get('dpi'),
                correo=request.POST.get('correo'),
                direccion=request.POST.get('direccion'),
                tipo_caso=request.POST.get('tipo_caso'),
                fecha_nacimiento=fecha_nacimiento
            )

            return redirect('/clientes/panel/?seccion=clientes')

        clientes = Cliente.objects.all()

    else:
        clientes = Cliente.objects.all()

    # ==================== AUDIENCIAS ====================
    if seccion == 'audiencias':
        if request.method == 'POST':
            cliente_id = request.POST.get('cliente')
            fecha = request.POST.get('fecha')

            if cliente_id:
                cliente = Cliente.objects.get(id=cliente_id)

                Audiencia.objects.create(
                    cliente=cliente,
                    fecha=fecha
                )

            return redirect('/clientes/panel/?seccion=audiencias')

        audiencias = Audiencia.objects.all()

    else:
        audiencias = Audiencia.objects.all()

    # ==================== EXPEDIENTES ====================
    if seccion == 'expedientes':
        if request.method == 'POST':
            cliente_id = request.POST.get('cliente')
            numero = request.POST.get('numero')
            tipo_caso = request.POST.get('tipo_caso')

            if cliente_id:
                cliente = Cliente.objects.get(id=cliente_id)

                Expediente.objects.create(
                    cliente=cliente,
                    numero=numero,
                    tipo_caso=tipo_caso
                )

            return redirect('/clientes/panel/?seccion=expedientes')

        expedientes = Expediente.objects.all()

    else:
        expedientes = Expediente.objects.all()

    return render(request, 'clientes/panel.html', {
        'clientes': clientes,
        'audiencias': audiencias,
        'expedientes': expedientes,
        'seccion': seccion
    })
