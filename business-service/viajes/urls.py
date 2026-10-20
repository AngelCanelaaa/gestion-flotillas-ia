from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViajeViewSet, GenerarResumenViajeView

router = DefaultRouter()
router.register(r'', ViajeViewSet, basename='viaje')

urlpatterns = [
    path('<int:viaje_id>/resumen/', GenerarResumenViajeView.as_view(), name='generar-resumen'),
    path('', include(router.urls)),
]