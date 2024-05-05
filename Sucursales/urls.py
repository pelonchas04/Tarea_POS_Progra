from django.urls import path, include
from Sucursales import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inicio/', views.inicio, name='inicio'),
    path('agregar/<int:dato_id>', views.Agregar_Producto, name='agregar'),
    path('sucursal/<int:dato_id>', views.Sucursal_Pantalla, name="sucursal"),
    path('pos/<int:dato_id>', views.Vender, name='vender'),
    path('comprar/<int:dato_id>', views.Comprar, name='comprar'),
    path('modificar/<int:dato_id>/<int:producto_id>', views.Modificar_Producto, name='modificar'),

    # path para usar redirect
    path('eliminar/<int:sucursal_id>/<int:p_id>', views.Eliminar_Producto, name="eliminar"),
    path('aproducto/<int:n_sucursal>', views.Agregar_Venta, name="aproducto")
]