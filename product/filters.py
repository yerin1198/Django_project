from django_filters import FilterSet, NumberFilter, CharFilter
from product.models import Product


class ProductFilter(FilterSet):
    price = NumberFilter()
    price__gt = NumberFilter(field_name="price", lookup_expr="gt")
    price__lt = NumberFilter(field_name="price", lookup_expr="lt")
    description = CharFilter(field_name="description", lookup_expr="icontains")  # 문자열 포함
    owner__name = CharFilter(field_name="owner", lookup_expr="username__icontains")
    class Meta:
        model = Product
        fields = ['price', 'description']

    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)

