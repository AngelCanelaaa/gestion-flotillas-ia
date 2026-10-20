from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeteccionFatigaCreateView, IncidenteViewSet, IncidenteHistorialView

router = DefaultRouter()
router.register(r'', IncidenteViewSet, basename='incidente')

urlpatterns = [
    path('detecciones/', DeteccionFatigaCreateView.as_view(), name='crear-deteccion'),
    path('<int:incidente_id>/historial/', IncidenteHistorialView.as_view(), name='historial-incidente'),
    path('', include(router.urls)),
]