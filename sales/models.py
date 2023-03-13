from django.db import models
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
    sellers = models.ManyToManyField(Sellers, verbose_name='فروشندگان طرح')
    description = models.TextField(null=True, verbose_name='توضیحات طرح')

    def __str__(self):
        return self.title

    def plan_status(self):
        if self.is_active:
            return format_html(f'<span class="badge bg-success">فعال</span>')
        else:
            return format_html(f'<span class="badge bg-danger">منقضی شده</span>')

    def sellers_list(self):
        out = '<ul class="list-group list-group-flush">'
        for i in self.sellers.all():
            out += f'<li class="list-group-item">{i.store_name}</li>'
        out += '</ul>'
        return format_html(out)


class Sells(models.Model):
    class Meta:
        verbose_name = 'فروش'
        verbose_name_plural = 'فروش ها'

    consumer = models.ForeignKey(Consumers, related_name='sell', verbose_name='مصرف کننده', on_delete=models.CASCADE)
    seller = models.ForeignKey(Sellers, related_name='sell', null=True, verbose_name='فروشنده', on_delete=models.SET_NULL)
    sale_plan = models.ForeignKey(SalesPlan, related_name='sell', verbose_name='طرح فروش', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.consumer} از {self.seller}'
