from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from accounts.mixins import SellerSuperuserMixin, FieldsMixin
from .models import SalesPlan, Sells


class HomeView(ListView):
    template_name = 'sales/index.html'
    queryset = SalesPlan.objects.all()


class PlanStoreDetailView(DetailView):
    template_name = 'sales/plan.html'
    model = SalesPlan


class SellCreate(SellerSuperuserMixin, FieldsMixin, LoginRequiredMixin, CreateView):
    template_name = 'sales/sell_register.html'
    model = Sells
    success_url = reverse_lazy('sales:plans_list')
