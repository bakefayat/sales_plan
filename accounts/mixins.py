from django.shortcuts import redirect

from core.utils import check_seller_superuser


class SellerSuperuserMixin:
    def dispatch(self, request, *args, **kwargs):
        if check_seller_superuser(request):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("sales:home")


class FormValidMixin:
    def form_valid(self, form):
        if self.request.is_superuser and self.request.is_authenticated:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.seller = self.request.user
            print(self.obj.seller)
        return super().form_valid(form)


class FieldsMixin:
    def dispatch(self, request, *args, **kwargs):
        self.fields = ('consumer', 'sale_plan')
        if request.user.is_superuser:
            self.fields.append('seller')
        return super().dispatch(request, *args, **kwargs)
