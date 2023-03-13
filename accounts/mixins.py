from django.shortcuts import redirect

from core.utils import check_seller_superuser


class SellerSuperuserMixin:
    def dispatch(self, request, *args, **kwargs):
        if check_seller_superuser(request):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("sales:home")

#
# class FormValidMixin:
#     def form_valid(self, form):
#         if self.request.is_superuser and self.request.is_authenticated:
#             form.save()
#         else:
#             self.obj = form.save(commit=False)
#             self.obj.seller = self.request.user
#             if not self.obj.status == "w":
#                 self.obj.status = "d"
#         return super().form_valid(form)
