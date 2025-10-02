# Amazon/urls.py (CÓDIGO CORREGIDO)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 🎯 CORRECCIÓN CLAVE: Ahora la ruta vacía ('') incluye las URLs de tu app Amasonsito.
    # Esto soluciona el 404 en la raíz y hace que la lista de productos sea la página de inicio.
    path('', include('Amasonsito.urls')), 

    # Rutas de Autenticación que no están dentro de la aplicación
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # El next_page lo he ajustado para que vuelva a la raíz (/) después del logout
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)