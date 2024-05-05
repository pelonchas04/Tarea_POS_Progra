from django import forms
from Sucursales import models

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["id_sucursal","nombre_producto", "precio_costo", "precio_venta", "existencias", "codigo_de_barras"]

class FormVenta(forms.ModelForm):
    class Meta:
        model = models.Venta
        fields = ["numero_de_venta", "id_sucursal"]

class FormListaVenta(forms.ModelForm):
    class Meta:
        model = models.ListaVentas
        fields = ["id_venta", "id_producto"]