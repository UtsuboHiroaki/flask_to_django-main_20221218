from django.contrib import admin

from .models import MetalPrice, MetalPurchase

# Register your models here.
admin.site.register(MetalPrice)
admin.site.register(MetalPurchase)
