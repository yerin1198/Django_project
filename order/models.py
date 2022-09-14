from django.db import models


class Order(models.Model):
    user = models.ForeignKey('user.User', verbose_name="사용자", on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', verbose_name="상품", on_delete=models.CASCADE)
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    quantity = models.IntegerField(verbose_name="수량")

    def __str__(self):  # 객체를 생성하면 문자열로 포함된 함수인 __str__이 호출됨.
        return str(self.user) + ' ' + str(self.product)

    class Meta:
        db_table = 'my_order'

