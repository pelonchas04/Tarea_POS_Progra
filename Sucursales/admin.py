from django.contrib import admin
from Sucursales import models

# Register your models here.

class SucursalAdmin(admin.ModelAdmin):
    list_display = ("nombre_sucursal",)
    search_fields = ("nombre_sucursal",)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre_producto", "codigo_de_barras", "id_sucursal")
    search_fields = ("codigo_de_barras",)

admin.site.register(models.Sucursal, SucursalAdmin)
admin.site.register(models.Producto, ProductoAdmin)