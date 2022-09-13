from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from product.models import Product
from product.pagination import ProductPagination
from product.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response("Swagger 연동 테스트")


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('-price', 'quantity')  # 가격 내림차순 -> 수량 오름차순 정렬
    pagination_class = ProductPagination
    permission_classes = [IsAuthenticatedOrReadOnly]  # 권한 추가
    authentication_classes = [BasicAuthentication, SessionAuthentication]  # 인증 추가

    def get_queryset(self):  # get_queryset 재정의
        q = self.request.query_params.get('price', '')
        name_q = self.request.query_params.get('name', '')
        description_q = self.request.query_params.get('description', '')
        qs = super().get_queryset()
        if q:
            qs = qs.filter(price__gt=q)
        if name_q:
            qs = qs.filter(name__icontains=name_q)
        if description_q:
            qs = qs.filter(description__icontains=description_q)

        return qs
