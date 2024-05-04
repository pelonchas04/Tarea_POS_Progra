from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Sucursal, Producto
from .forms import FormularioProducto
from django.contrib.auth.decorators import login_required


# @login_required
def inicio(request):
    datos = Sucursal.objects.all() # consulta a la base de datos
    return render(request, 'InicioEnSucursal.html', {"Sucursales": datos})


# @login_required
def Sucursal_Pantalla(request, dato_id):
    dato = get_object_or_404(Sucursal, pk = dato_id) # buscamos por id la sucursal a trabajar en forma de objeto
    numero_de_sucursal = dato.id


    productos_de_sucursal = Producto.objects.filter(id_sucursal__icontains = numero_de_sucursal)

    return render(request, 'PantallaSucural.html', {"productos": productos_de_sucursal, "Sucursal": dato})


def Agregar_Producto(request, dato_id):
    if request.method == "POST":
        dato = get_object_or_404(Sucursal,pk =  dato_id) # guarda el numero de sucursal
        el_producto = FormularioProducto(request.POST)
        if el_producto.is_valid():
            mensaje = "Producto ingresado correctamente"
            el_producto.save()
            return render(request, 'AgregarProducto.html', {"numeroS": dato.id, "mensaje": mensaje})
        else:
            mensaje = "Llene todos los campos"
        
        return render(request, 'AgregarProducto.html', {"numeroS": dato.id, "mensaje": mensaje})
    else:
        el_producto = FormularioProducto()
        return render(request, 'AgregarProducto.html', {"numeroS": dato.id, "mensaje": ""})
    

def Modificar_Producto(request, dato_id, producto_id):
    dato = get_object_or_404(Sucursal, pk = dato_id)

    return render(request, 'ModificarProducto.html', {"numeroS": dato.id})

def Vender(request, dato_id):

    dato = get_object_or_404(Sucursal,pk =  dato_id)
    return render(request, 'Ventas.html')

def Comprar(request, dato_id):

    dato = get_object_or_404(Sucursal,pk =  dato_id)
    return render(request, "Compras.html")