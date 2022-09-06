from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from product.filters import ProductFilter
from product.models import Product
from product.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response("Swagger 연동 테스트")


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ProductFilter
    filterset_fields = ['name']


