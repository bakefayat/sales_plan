from django.db import models
from consumers.models import Consumers
from core.models import TimeStampedModel


class Sellers(models.Model):
    class Meta:
        verbose_name = 'فروشنده'
        verbose_name_plural = 'فروشندگان'

    store_name = models.CharField(max_length=255, verbose_name='نام واحد تجاری')
    address = models.TextField(verbose_name='آدرس')
    phone_number = models.CharField(max_length=12, verbose_name='تلفن تماس')

    def __str__(self):
        return self.store_name


class SalesPlan(TimeStampedModel):
    class Meta:
        verbose_name = 'طرح فروش'
        verbose_name_plural = 'طرح های فروش'

    consumer = models.ManyToManyField(Consumers, related_name='plans', verbose_name='مصرف کننده')
    seller = models.ManyToManyField(Sellers, related_name='seller', verbose_name='فروشنده')

    # def __str__(self):
    #     return self.seller
