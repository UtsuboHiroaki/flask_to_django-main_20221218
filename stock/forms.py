from django import forms

from stock.models import StockPurchase


class StockPurchaseForm(forms.ModelForm):
    class Meta:
        model = StockPurchase
        fields = ['stock_type', 'weight', 'email', 'name', ]
        widgets = {
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_type': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
