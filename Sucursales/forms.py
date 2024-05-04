from django import forms
from Sucursales.models import Producto

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["id_sucursal","nombre_producto", "precio_costo", "precio_venta", "existencias", "codigo_de_barras"]