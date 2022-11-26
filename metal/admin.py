from django.contrib import admin

from .models import MetalType, MetalPurchase

# Register your models here.
admin.site.register(MetalType)
admin.site.register(MetalPurchase)
