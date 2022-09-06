from product.views import TestView
from django.urls import path
from .views import ProductViewSet
from product import views
from rest_framework.urlpatterns import format_suffix_patterns

product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
urlpatterns = [
    path('v1/product/', product_list),
    path('v1/<int:pk>/', product_detail),
    path('v1/test/', TestView.as_view(), name='test'),
]