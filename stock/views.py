from django.contrib import messages
from django.shortcuts import resolve_url, render, redirect
from django.views.generic import ListView, CreateView

from stock.forms import StockPurchaseForm
from stock.models import StockPrice


class StockTopView(ListView):
    model = StockPrice
    template_name = 'stock/index.html'


def stock_buy(request):
    if request.method == 'POST':
        form = StockPurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '毎度ありがとうございます！')
            return redirect('main:thanks')
        else:
            for key, value in form.errors.items():
                messages.warning(request, f'{key}:{value[0]}')
    else:
        form = StockPurchaseForm()
    return render(request, 'stock/buy.html', {'form': form})


class StockBuy(CreateView):
    form_class = StockPurchaseForm
    template_name = 'stock/buy.html'

    def form_invalid(self, form):
        for key, value in form.errors.items():
            messages.warning(self.request, f'{key}:{value[0]}')
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, '毎度ありがとうございます！')
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url('main:thanks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stocks'] = StockPrice.objects.all()
        return context
