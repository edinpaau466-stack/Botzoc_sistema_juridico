from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return render(request, 'bufete.html')

urlpatterns = [
    path('', home, name='home'),
    path('clientes/', include('clientes.urls')),
    path('biblioteca/', include('biblioteca.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
