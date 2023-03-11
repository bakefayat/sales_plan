from django.contrib import admin
from sales.models import Sellers, SalesPlan, Sells


class SalesPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'total_capacity', 'description')


admin.site.register(Sellers)
admin.site.register(SalesPlan, SalesPlanAdmin)
admin.site.register(Sells)
