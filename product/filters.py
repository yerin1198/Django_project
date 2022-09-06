from django_filters import FilterSet, NumberFilter, CharFilter, OrderingFilter

from product.models import Product


class ProductFilter(FilterSet):
    class Meta:
        price = NumberFilter()
        price__gt = NumberFilter(field_name='price', lookup_expr="gt")
        price__lt = NumberFilter(field_name='price', lookup_expr="lt")
        description = CharFilter(field_name='description', lookup_expr="icontains")  # 문자열 포함

        class Meta:
            model = Product
            fields = ["price", "description"]

        order_by_field = 'ordering'
        ordering = OrderingFilter(
            fields=(
                'price',
            )
        )

