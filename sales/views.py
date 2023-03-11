from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import SalesPlan, Sellers


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
