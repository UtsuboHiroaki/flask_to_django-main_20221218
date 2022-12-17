from django.urls import path

from . import views

app_name = 'metal'
urlpatterns = [
    path('', views.redirect_func, name='redirect'),

    path('index/', views.MetalTopView.as_view(), name='index'),
    path('_index/', views.metal_top_view, name='func_index'),

    path('item/<int:pk>/', views.MetalDetail.as_view(), name='detail'),

    path('buy/', views.MetalBuy.as_view(), name='buy'),
    path('_buy/', views.metal_buy_view, name='func_buy'),

    path('purchase_list/', views.MetalPurchaseList.as_view(), name='purchase_list'),

    path('api/info/', views.MetalAllInfoAPI.as_view(), name='allinfo'),
    path('api/info/buy/', views.metal_buy_api, name='buyapi'),
    path('api/info/<str:type_name>/', views.MetalInfoAPI.as_view(), name='info'),
]
