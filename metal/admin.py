from django.contrib import admin

from .models import Metal, MetalPurchase

# Register your models here.
admin.site.register(Metal)
admin.site.register(MetalPurchase)
