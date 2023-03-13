from django.contrib import admin
from django.contrib.auth import get_user_model as User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'is_superuser',
        'is_seller',
    ]


admin.site.register(User(), UserAdmin)
