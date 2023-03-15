from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.html import format_html
from django.contrib.auth import get_user_model as User

from consumers.models import Consumers
from core.models import TimeStampedModel


class Sellers(models.Model):
    class Meta:
        verbose_name = 'فروشنده'
        verbose_name_plural = 'فروشندگان'

    user = models.OneToOneField(User(), on_delete=models.CASCADE, verbose_name='کاربر فروشنده')
    store_name = models.CharField(max_length=255, verbose_name='نام واحد تجاری')
    address = models.TextField(verbose_name='آدرس')
    phone_number = models.CharField(max_length=12, verbose_name='تلفن تماس')

    def __str__(self):
        return self.store_name


class SalesPlan(TimeStampedModel):
    class Meta:
        verbose_name = 'طرح فروش'
        verbose_name_plural = 'طرح های فروش'

    title = models.CharField(max_length=255, verbose_name='نام طرح')
    is_active = models.BooleanField(default=True, verbose_name='فعال بودن')
    total_capacity = models.IntegerField(verbose_name='حداکثر ظرفیت طرح')
    description = models.TextField(null=True, verbose_name='توضیحات طرح')

    def __str__(self):
        return self.title

    def plan_status(self):
        if self.is_active:
            return format_html(f'<span class="badge bg-success">فعال</span>')
        else:
            return format_html(f'<span class="badge bg-danger">منقضی شده</span>')


class Sells(TimeStampedModel):
    class Meta:
        verbose_name = 'فروش'
        verbose_name_plural = 'فروش ها'

    consumer = models.ForeignKey(Consumers, related_name='sell', verbose_name='مصرف کننده', on_delete=models.CASCADE)
    seller = models.ForeignKey(Sellers, related_name='sell', null=True, verbose_name='فروشنده', on_delete=models.SET_NULL)
    sale_plan = models.ForeignKey(SalesPlan, related_name='sell', null=True, verbose_name='طرح فروش', on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=True, verbose_name='یکبار تلاش برای خرید')

    def __str__(self):
        return f'{self.consumer} از {self.seller}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        sells = Sells.objects.filter(consumer=self.consumer).filter(sale_plan=self.sale_plan)
        if sells:
            self.is_valid = False
            print('دوباره ثبت نام کرده است.')
        super().save(*args, **kwargs)
