from django.contrib import messages
from django.shortcuts import resolve_url
from django.views.generic import ListView, CreateView

from stock.forms import StockPurchaseForm
from stock.models import StockPrice


class StockTopView(ListView):
    model = StockPrice
    template_name = 'stock/index.html'


class StockBuy(CreateView):
    form_class = StockPurchaseForm
    template_name = 'stock/buy.html'

    def form_invalid(self, form):
        for key, value in form.errors.items():
            messages.warning(self.request, f'{key}:{value[0]}')
        return super().form_invalid(form)

    def get_success_url(self):
        return resolve_url('main:thanks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stocks'] = StockPrice.objects.all()
        return context
