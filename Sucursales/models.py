from django.db import models

class Sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=50)
    
class Producto(models.Model):
    id_sucursal = models.IntegerField()
    nombre_producto = models.CharField(max_length=50)
    precio_costo = models.FloatField()
    precio_venta = models.FloatField()
    existencias = models.IntegerField()
    codigo_de_barras = models.CharField(max_length=20)

class Venta(models.Model):
    numero_de_venta = models.IntegerField()
    id_sucursal = models.IntegerField()
    estado = models.BooleanField()

class ListaVentas(models.Model):
    id_venta = models.IntegerField()
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()