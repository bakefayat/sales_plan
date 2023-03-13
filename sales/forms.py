from django import forms
from .models import Sells


class SellRegister(forms.ModelForm):
    class Meta:
        model = Sells
