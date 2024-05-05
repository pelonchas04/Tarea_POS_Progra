from django.shortcuts import render, get_object_or_404, redirect
from .models import Sucursal, Producto, Venta, ListaVentas
from .forms import FormularioProducto, FormVenta, FormListaVenta
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
    dato = Sucursal.objects.get(id = dato_id)
    if request.method == "GET":
         # guarda el numero de sucursal
        el_producto = FormularioProducto(request.GET)
        if el_producto.is_valid():
            mensaje = "Producto ingresado correctamente"
            el_producto.save()
            return render(request, 'AgregarProducto.html', {"numeroS": dato.id, "mensaje": mensaje})
        else:
            mensaje = "Llene todos los campos"
        
        return render(request, 'AgregarProducto.html', {"numeroS": dato.id, "mensaje": mensaje})
    else:
        return render(request, 'AgregarProducto.html', {"numeroS": dato.id, "mensaje": ""})
    

def Modificar_Producto(request, dato_id, producto_id):
    dato = get_object_or_404(Sucursal, pk = dato_id)
    producto = Producto.objects.get(id = producto_id)
    if request.method == "GET":
        form_producto = FormularioProducto(request.GET)
        if form_producto.is_valid():
            mensaje = "Producto guardado exitosamente"


            producto.nombre_producto = request.GET['nombre_producto']
            producto.precio_costo = request.GET['precio_costo']
            producto.precio_venta = request.GET['precio_venta']
            producto.existencias = request.GET['existencias']
            producto.codigo_de_barras = request.GET['codigo_de_barras']
            
            producto.save()
            return render(request, 'ModificarProducto.html', {"numeroS": dato.id, "Producto": producto, "mensaje": mensaje})
        else:
            mensaje = "Llene todos los campos"
            return render(request, 'ModificarProducto.html', {"numeroS": dato.id, "Producto": producto, "mensaje": mensaje})
        
    mensaje = ""

    return render(request, 'ModificarProducto.html', {"numeroS": dato.id, "Producto": producto, "mensaje":mensaje})

def Eliminar_Producto(request, sucursal_id, p_id):
    producto_eliminar = Producto.objects.get(id = p_id)
    producto_eliminar.delete()


    return redirect('sucursal', dato_id = sucursal_id)


def Vender(request, dato_id):
    sucursal = Sucursal.objects.get(id = dato_id)
    venta = Venta()
    lista_ventas = Venta.objects.all()

    if len(lista_ventas) ==0:
        venta.id = 1
        venta.numero_de_venta = 1
        venta.id_sucursal = sucursal.id
        venta.estado = False
    else:
        ultima = lista_ventas.last()
        venta.id = ultima.id + 1
        venta.numero_de_venta = ultima.numero_de_venta + 1
        venta.id_sucursal = sucursal.id
        venta.estado = False
    
    venta.save()

    lista_productos_venta = ListaVentas.objects.filter(id_venta = venta.id)


    if len(lista_productos_venta) == 0:
        mensaje1 = "Ingrese el codigo de barras de los productos"
        return render(request, 'Ventas.html', {"mensaje": mensaje1, "numeroS": sucursal.id, "venta": venta})
    else:   
        mensaje1 = ""

    mensaje2 =""
    return render(request, 'Ventas.html', {"mensaje": mensaje1, "numeroS": sucursal.id, "venta": venta, "advertencia": mensaje2})

def Agregar_Venta(request, n_sucursal):
    sucursal = Sucursal.objects.get(id = n_sucursal)
    lista_ventas = ListaVentas()

    if request.method == "GET":
        # lista_venta = ListaVentas()
        # lista_venta.id_venta = request.GET["id_venta"]
        #  = Producto.objects.get(codigo_de_barras = request.GET["codigo"])

        # buscar_producto = Producto.objects.get(codigo_de_barras = request.GET["codigo"])
        # if buscar_producto == 0:
        #     return redirect('pos/', dato_id = sucursal.id)

        try:
            buscar_producto = Producto.objects.get(codigo_de_barras = request.GET["codigo"])

            lista_ventas.id_venta = request.GET["id_venta"]
            lista_ventas.id_producto = buscar_producto.id

            lista_ventas.save()
        except Producto.DoesNotExist:
            return redirect('vender', dato_id = sucursal.id)
            

    return redirect('vender', dato_id = sucursal.id)


def Comprar(request, dato_id):

    dato = get_object_or_404(Sucursal,pk =  dato_id)
    return render(request, "Compras.html")