from django.shortcuts import redirect

from core.utils import check_seller_superuser


class SellerSuperuserMixin:
    def dispatch(self, request, *args, **kwargs):
        if check_seller_superuser(request):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("sales:home")
