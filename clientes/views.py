from django.shortcuts import render

# HOME
def home(request):
    return render(request, 'clientes/home.html')

# PANEL
def panel(request):
    return render(request, 'clientes/panel.html')
