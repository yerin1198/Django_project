from product.views import TestView
from product.views import ProductList
from django.urls import path
from product import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('v1/product/', views.ProductList.as_view()),
    path('v1/<int:pk>/', views.ProductDetail.as_view()),
    path('v1/test/', TestView.as_view(), name='test'),
]