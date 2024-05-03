from django.shortcuts import render, get_object_or_404
from .models import Sucursal

numero_de_sucursal = 0

def inicio(request):
    datos = Sucursal.objects.all()
    return render(request, 'InicioEnSucursal.html', {"Sucursales": datos})

def Sucursal_Pantalla(request, dato_id):
    dato = get_object_or_404(Sucursal, pk = dato_id)
    return render(request, 'PantallaSucural.html', {"dato": dato})