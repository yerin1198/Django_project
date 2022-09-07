from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()  # 상품 상세 설명
    quantity = models.IntegerField()  # 재고


