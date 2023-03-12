from django import forms
from .models import SalesPlan, Sells


class SellRegister(forms.ModelForm):
    class Meta:
        model = Sells
        fields = ('consumer', 'seller', 'sale_plan')

    def __init__(self, *args, **kwargs):
        super(SellRegister, self).__init__(*args, **kwargs)
