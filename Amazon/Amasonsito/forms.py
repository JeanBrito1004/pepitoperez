# Amasonsito/forms.py

from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    """
    Formulario basado en el modelo Producto para la creación rápida.
    """
    class Meta:
        model = Producto
        # Define los campos que el usuario podrá llenar
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen'] 
        # Opcional: añade widgets para mejorar la apariencia de los campos
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
        }