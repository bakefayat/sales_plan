from django.shortcuts import redirect

from core.utils import check_seller_superuser
from sales.models import Sellers, SalesPlan


class SellerSuperuserMixin:
    def dispatch(self, request, *args, **kwargs):
        if check_seller_superuser(request):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("login")


class FormValidMixin:
    def form_valid(self, form):
        if self.request.user.is_superuser and self.request.user.is_authenticated:
            form.save()
        else:
            self.obj = form.save(commit=False)
            seller = Sellers.objects.filter(user=self.request.user).first()
            sale_plan = SalesPlan.objects.filter(pk=self.kwargs.pop('pk')).first()
            self.obj.seller = seller
            self.obj.sale_plan = sale_plan
        return super().form_valid(form)


class FieldsMixin:
    def __init__(self):
        self.fields = ['consumer']

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields.append('seller')
        return super().dispatch(request, *args, **kwargs)
