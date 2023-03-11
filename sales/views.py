from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import SalesPlan, Sellers


class HomeView(ListView):
    template_name = 'sales/index.html'
    queryset = SalesPlan.objects.all()


class PlanStoreListView(DetailView):
    # def get_queryset(self):
    #     plan_id = self.kwargs.get('pk')
    #     plan = get_object_or_404(SalesPlan, pk=plan_id)
    #     return plan

    template_name = 'sales/plan.html'
    model = SalesPlan