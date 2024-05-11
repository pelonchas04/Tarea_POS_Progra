from django.contrib import admin
from Sucursales import models

# Register your models here.

class VentasAdmin(admin.ModelAdmin):
    list_display = ("id","numero_de_venta", "estado", "id_sucursal")
    search_fields = ("numero_de_venta",)

class ListaVentasAdmin(admin.ModelAdmin):
    list_display = ("id", "id_venta", "id_producto")
    search_fields = ("id",)

class SucursalAdmin(admin.ModelAdmin):
    list_display = ("nombre_sucursal",)
    search_fields = ("nombre_sucursal",)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre_producto", "codigo_de_barras", "id_sucursal")
    search_fields = ("codigo_de_barras",)

admin.site.register(models.Sucursal, SucursalAdmin)
admin.site.register(models.Producto, ProductoAdmin)
admin.site.register(models.Venta, VentasAdmin)
admin.site.register(models.ListaVentas, ListaVentasAdmin)