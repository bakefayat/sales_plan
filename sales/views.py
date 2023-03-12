from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import SellRegister
from .models import SalesPlan, Sellers, Sells


class HomeView(ListView):
    template_name = 'sales/index.html'
    queryset = SalesPlan.objects.all()


class PlanStoreListView(DetailView):
    # def get_context_data(self, **kwargs):
    #     pk = self.kwargs.get("pk")
    #     item = get_object_or_404(SalesPlan, pk=pk)
    #     sellers = item.sellers.all()
    #
    #     context = super().get_context_data(**kwargs)
    #     context['sellers'] = sellers

    template_name = 'sales/plan.html'
    model = SalesPlan


class SellCreate(CreateView):
    template_name = 'sales/sell_register.html'
    form_class = SellRegister
    model = Sells
    success_url = reverse_lazy('sales:plans_list')
