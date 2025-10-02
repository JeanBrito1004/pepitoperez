# Amasonsito/views.py (CÓDIGO FINAL CORREGIDO)

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.shortcuts import render 
from django.urls import reverse_lazy 
from .models import Producto # Asumiendo que Producto es tu modelo
from .forms import ProductoForm # Necesitas ESTE ARCHIVO (ProductoForm)

# 1. Vista para listar productos
class ListaProductosView(LoginRequiredMixin, ListView): 
    model = Producto
    template_name = 'productos/lista.html'
    context_object_name = 'productos'

# 2. Vista para el Detalle de un Producto
class DetalleProductoView(DetailView):
    model = Producto
    template_name = 'productos/detalle_producto.html'
    context_object_name = 'producto'

# 3. Vista para Crear un Producto (NUEVA)
class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm 
    template_name = 'productos/crear_producto.html'
    # Redirecciona a la lista de productos después de guardar
    success_url = reverse_lazy('lista_productos')
    
# 4. Función para la página de éxito después del cambio de contraseña
def contrasena_actualizada(request):
    """Muestra una página simple de éxito."""
    return render(request, 'contrasena_actualizada.html', {})