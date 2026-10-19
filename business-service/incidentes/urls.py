from django.urls import path
from .views import DeteccionFatigaCreateView

urlpatterns = [
    path('detecciones/', DeteccionFatigaCreateView.as_view(), name='crear-deteccion'),
]