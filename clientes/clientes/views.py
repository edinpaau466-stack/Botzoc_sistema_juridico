from django.shortcuts import render, redirect
from .models import Cliente

def clientes_view(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        direccion = request.POST.get("direccion")
        Cliente.objects.create(nombre=nombre, direccion=direccion)
        return redirect("/clientes/")

    clientes = Cliente.objects.all()
    return render(request, "clientes.html", {"clientes": clientes})
