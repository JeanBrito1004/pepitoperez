# Amasonsito/urls.py (CÓDIGO FINAL CORREGIDO)

from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import (
    ListaProductosView, 
    DetalleProductoView, 
    ProductoCreateView, # <-- Importar la nueva vista de creación
    contrasena_actualizada
)

urlpatterns = [
    # 🏠 1. Página de inicio (http://127.0.0.1:8000/)
    path('', ListaProductosView.as_view(), name='lista_productos'),
    
    # 🎯 2. NUEVA URL DE CREACIÓN
    path('crear/', ProductoCreateView.as_view(), name='crear_producto'), 
    
    # 3. URL DE DETALLE
    path('<int:pk>/', DetalleProductoView.as_view(), name='detalle_producto'), 
    
    # 4. URL de Cambio de Contraseña
    path(
        'cambiar-contrasena/', 
        auth_views.PasswordChangeView.as_view(
            template_name='cambiar_contrasena.html',
            success_url='/Amasonsito/perfil-actualizado/' 
        ), 
        name='cambiar_contrasena'
    ),
    
    # 5. URL de Éxito después del cambio de contraseña
    path('perfil-actualizado/', contrasena_actualizada, name='perfil_actualizado'), 
]