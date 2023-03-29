from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.db import IntegrityError
from django.shortcuts import render

from accounts.mixins import SellerSuperuserMixin, FieldsMixin, FormValidMixin
from .models import SalesPlan, Sells


class HomeView(ListView):
    template_name = 'sales/index.html'
    queryset = SalesPlan.objects.all()


class PlanStoreDetailView(DetailView):
    template_name = 'sales/plan.html'
    model = SalesPlan


class SellCreate(LoginRequiredMixin, SellerSuperuserMixin, FormValidMixin, FieldsMixin, CreateView):
    template_name = 'sales/sell_register.html'
    model = Sells
    success_url = reverse_lazy('sales:plans_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            consumer = form.cleaned_data.get('consumer')
            obj = Sells.objects.filter(consumer=consumer).first()
            ctx = {'consumer': obj}
            print('hello')
            print(ctx['consumer'])
            return render(self.request, 'sales/twice_buy_error.html', ctx)
