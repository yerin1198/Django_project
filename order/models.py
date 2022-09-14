from django.db import models


class Order(models.Model):
    user = models.ForeignKey('user.User', verbose_name="사용자", on_delete=models.CASCADE) #참조하는 대상의 id값을 가져옴.
    product = models.ForeignKey('product.Product', verbose_name="상품", on_delete=models.CASCADE) #장고에서 1:n 관계에서 fk는 n쪽에 명시.
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    quantity = models.IntegerField(verbose_name="수량")

    def __str__(self):  # 객체를 생성하면 문자열로 포함된 함수인 __str__이 호출됨.
        return str(self.user) + ' ' + str(self.product)



