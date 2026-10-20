from django.urls import re_path
from .views import GatewayProxyView

urlpatterns = [
    re_path(r'^api/(?P<path>.*)$', GatewayProxyView.as_view()),
]