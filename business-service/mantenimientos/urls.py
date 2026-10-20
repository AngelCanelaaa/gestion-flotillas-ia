from rest_framework.routers import DefaultRouter
from .views import MantenimientoViewSet

router = DefaultRouter()
router.register(r'', MantenimientoViewSet, basename='mantenimiento')

urlpatterns = router.urls