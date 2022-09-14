from product.views import TestView
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/test/', TestView.as_view(), name='test'),
]