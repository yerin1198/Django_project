from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters

from product.filters import ProductFilter
from product.models import Product
from product.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 2


class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response("Swagger 연동 테스트")


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [filters.OrderingFilter]
    filter_class = ProductFilter
    pagination_class = ProductPagination
    #filterset_fields = ['name', 'id']
    ordering_fields = ['price']  # 정렬 대상이 될 field 지정
    ordering = ['id']  # Default 정렬 기준 지정

    def get_queryset(self):
        return super().get_queryset().filter()
