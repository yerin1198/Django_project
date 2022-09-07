from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from product.models import Product
from product.pagination import ProductPagination
from product.serializers import ProductSerializer


class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response("Swagger 연동 테스트")


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('-price', 'quantity')  # 가격 내림차순 -> 수량 오름차순 정렬
    pagination_class = ProductPagination

    def get_queryset(self):  # get_queryset 재정의
        q = self.request.query_params.get('search', '')
        qs = super().get_queryset()
        if q:
            qs = qs.filter(price__gt=q)
        return qs
