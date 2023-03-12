from django import forms
from .models import SalesPlan, Sells


class SellRegister(forms.ModelForm):
    class Meta:
        model = Sells
        fields = ('consumer', 'seller', 'sale_plan')
