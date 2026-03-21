from django.shortcuts import render
from .models import Cliente, Audiencia, Expediente

def panel(request):
    seccion = request.GET.get('seccion', 'clientes')

    clientes = Cliente.objects.all()
    audiencias = Audiencia.objects.all()
    expedientes = Expediente.objects.all()

    return render(request, 'clientes/panel.html', {
        'clientes': clientes,
        'audiencias': audiencias,
        'expedientes': expedientes,
        'seccion': seccion
    })
