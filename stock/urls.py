from django.urls import path
from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.RedirectToIndex.as_view(), name='redirect'),
    path('index/', views.StockTopView.as_view(), name='index'),
    path('item/<int:pk>/', views.stock_detail, name='detail'),
    path('buy/', views.StockBuy.as_view(), name='buy'),
    path('_buy/', views.stock_buy, name='buy_func'),
]
