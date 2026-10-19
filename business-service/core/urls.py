from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vehiculos/', include('vehiculos.urls')),
    path('api/choferes/', include('choferes.urls')),
    path('api/viajes/', include('viajes.urls')),
]