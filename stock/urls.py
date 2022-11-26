from django.urls import path
from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.StockTopView.as_view(), name='index'),
    path('buy/', views.StockBuy.as_view(), name='buy'),
]
