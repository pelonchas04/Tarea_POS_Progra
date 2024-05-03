from django.urls import path, include
from Sucursales import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inicio/', views.inicio,name='inicio'),
    path('sucursal/<int:dato_id>', views.Sucursal_Pantalla, name="sucursal"),
]