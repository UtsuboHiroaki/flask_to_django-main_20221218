from django.contrib import admin

from .models import StockPrice, StockPurchase


@admin.register(StockPrice)
class StockPriceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'buy', 'sell')


@admin.register(StockPurchase)
class StockPurchaseAdmin(admin.ModelAdmin):
    list_display = ('stock_price', 'weight', 'email', 'name', 'created')
    list_filter = ('stock_price', 'created')
    search_fields = ('stock_price__company_name', 'email', 'name', 'created')

