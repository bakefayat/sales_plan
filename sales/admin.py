from django.contrib import admin
from sales.models import Sellers, SalesPlan, Sells


class SalesPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'total_capacity', 'description', 'sellers_list')


class SellersAdmin(admin.ModelAdmin):
    list_display = ('user', 'store_name')


admin.site.register(Sellers, SellersAdmin)
admin.site.register(SalesPlan, SalesPlanAdmin)
admin.site.register(Sells)
