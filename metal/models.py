from django.db import models


# Create your models here.
class Metal(models.Model):
    """
    貴金属の情報

    1gあたりの価格を示す
    """

    name = models.CharField(verbose_name="金属名", max_length=100)
    buy = models.PositiveIntegerField(verbose_name="買値", null=True, blank=True)
    sell = models.PositiveIntegerField(verbose_name='売値', null=True, blank=True)

    def __str__(self):
        return self.name


class MetalPurchase(models.Model):
    """
    貴金属の買取履歴
    """

    metal = models.ForeignKey(Metal, verbose_name="金属名", on_delete=models.PROTECT)
    weight = models.PositiveIntegerField(verbose_name="重量", null=True, blank=True)
    email = models.CharField(verbose_name="email", max_length=255)
    name = models.CharField(verbose_name="取引者", max_length=255)
    created = models.DateTimeField(verbose_name="取引日時", auto_now_add=True)

    def __str__(self):
        return f'{str(self.metal)}_{str(self.created)}'
