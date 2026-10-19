from rest_framework.routers import DefaultRouter
from .views import ChoferViewSet

router = DefaultRouter()
router.register(r'', ChoferViewSet, basename='chofer')

urlpatterns = router.urls