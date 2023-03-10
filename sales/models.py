from django.db import models
from consumers.models import Consumers
from core.models import TimeStampedModel


class SalesPlan(TimeStampedModel):
    class Meta:
        verbose_name = 'طرح فروش'
        verbose_name_plural = 'طرح های فروش'

    title = models.CharField(max_length=255, verbose_name='نام طرح')
    is_active = models.BooleanField(default=True, verbose_name='فعال بودن')
    total_capacity = models.IntegerField(verbose_name='حداکثر ظرفیت طرح')
    total_sales = models.IntegerField(default=0, verbose_name='تعداد شرکت کنندگان')

    def __str__(self):
        return self.title


class Sellers(models.Model):
    class Meta:
        verbose_name = 'فروشنده'
        verbose_name_plural = 'فروشندگان'

    store_name = models.CharField(max_length=255, verbose_name='نام واحد تجاری')
    address = models.TextField(verbose_name='آدرس')
    phone_number = models.CharField(max_length=12, verbose_name='تلفن تماس')

    def __str__(self):
        return self.store_name


class Sells(models.Model):
    class Meta:
        verbose_name = 'فروش'
        verbose_name_plural = 'فروش ها'

    consumer = models.ForeignKey(Consumers, related_name='sell', unique=True, verbose_name='مصرف کننده', on_delete=models.CASCADE)
    seller = models.ForeignKey(Sellers, related_name='sell', null=True, verbose_name='فروشنده', on_delete=models.SET_NULL)
    sale_plan = models.ForeignKey(SalesPlan, related_name='sell', verbose_name='طرح فروش', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.consumer} از {self.seller}'
