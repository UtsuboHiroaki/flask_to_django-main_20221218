from django.contrib import admin

from .models import Stock, StockPurchase


@admin.register(Stock)
class StockTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'buy', 'sell')


@admin.register(StockPurchase)
class StockPurchaseAdmin(admin.ModelAdmin):
    list_display = ('stock', 'weight', 'email', 'name', 'created')
    list_filter = ('stock', 'created')
    search_fields = ('stock__company_name', 'email', 'name', 'created')
