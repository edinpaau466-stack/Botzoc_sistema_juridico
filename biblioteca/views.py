from django.shortcuts import render
from .models import Ley

def biblioteca(request):
    leyes = Ley.objects.all()
    return render(request, 'biblioteca.html', {'leyes': leyes})
