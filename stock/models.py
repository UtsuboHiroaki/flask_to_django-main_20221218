from django.db import models
from django.utils import timezone


class Stock(models.Model):
    """
    株価の情報
    """

    name = models.CharField(verbose_name="銘柄名", max_length=100)
    buy = models.PositiveIntegerField(verbose_name="買値", null=True, blank=True)
    sell = models.PositiveIntegerField(verbose_name='売値', null=True, blank=True)

    def __str__(self):
        return self.name


class StockPurchase(models.Model):
    """
    株の買取履歴
    """

    stock = models.ForeignKey(Stock, verbose_name="銘柄名", on_delete=models.PROTECT)
    weight = models.PositiveIntegerField(verbose_name="株数", )
    email = models.EmailField(verbose_name="連絡先メールアドレス", max_length=255)
    name = models.CharField(verbose_name="お名前", max_length=255)
    created = models.DateTimeField(verbose_name="取引日時", default=timezone.now)

    def __str__(self):
        return f'{str(self.stock)}_{str(self.created)}'
