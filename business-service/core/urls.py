from django.contrib import admin
from django.urls import include, path
# NUEVO: Importaciones para Swagger
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas de tus microservicios
    path('api/vehiculos/', include('vehiculos.urls')),
    path('api/choferes/', include('choferes.urls')),
    path('api/viajes/', include('viajes.urls')),
    path('api/incidentes/', include('incidentes.urls')),
    path('api/rutas/', include('rutas.urls')),
    path('api/mantenimientos/', include('mantenimientos.urls')),
    
    # NUEVO: Rutas de Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]