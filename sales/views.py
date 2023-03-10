from django.shortcuts import render
from django.views.generic import ListView
from .models import SalesPlan


class HomeView(ListView):
    template_name = 'sales/index.html'
    queryset = SalesPlan.objects.all()
