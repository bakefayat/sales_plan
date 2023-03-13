from django.contrib import admin
from django.contrib.auth import get_user_model as User

from sales.models import Sellers


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'is_superuser',
        'is_seller',
    ]

    def is_seller(self, obj):
        if Sellers.objects.filter(user=obj):
            return '+'
        return '-'

    is_seller   .short_description = 'فروشنده'


admin.site.register(User(), UserAdmin)
