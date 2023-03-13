from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import SellRegister
from .models import SalesPlan, Sellers, Sells


class HomeView(ListView):
    template_name = 'sales/index.html'
    queryset = SalesPlan.objects.all()


class PlanStoreDetailView(DetailView):
    template_name = 'sales/plan.html'
    model = SalesPlan


class SellCreate(LoginRequiredMixin, CreateView):
    template_name = 'sales/sell_register.html'
    form_class = SellRegister
    model = Sells
    success_url = reverse_lazy('sales:plans_list')
