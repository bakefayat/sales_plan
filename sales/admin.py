from django.contrib import admin
from sales.models import Sellers, SalesPlan, Sells


class SalesPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'total_capacity', 'description')


class SellersAdmin(admin.ModelAdmin):
    list_display = ('user', 'store_name', 'address')


class SellsAdmin(admin.ModelAdmin):
    list_display = ('consumer', 'sale_plan', 'seller', 'created')


admin.site.register(Sellers, SellersAdmin)
admin.site.register(SalesPlan, SalesPlanAdmin)
admin.site.register(Sells, SellsAdmin)
