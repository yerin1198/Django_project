from django_filters import (
    FilterSet,
    CharFilter,
    NumberFilter,
)

from .models import Product


class ProductFilter(FilterSet):
    price = NumberFilter()
    price__gt = NumberFilter(field_name="price", lookup_expr="gt")
    price__lt = NumberFilter(field_name="price", lookup_expr="lt")
    description = CharFilter(lookup_expr="icontains")  # 문자열 포함

    class Meta:
        model = Product
        fields = ["price", "description"]

    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
