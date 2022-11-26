from django.contrib import admin

from .models import StockType, StockPurchase


@admin.register(StockType)
class StockTypeAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'buy', 'sell')


@admin.register(StockPurchase)
class StockPurchaseAdmin(admin.ModelAdmin):
    list_display = ('stock_type', 'weight', 'email', 'name', 'created')
    list_filter = ('stock_type', 'created')
    search_fields = ('stock_type__company_name', 'email', 'name', 'created')

