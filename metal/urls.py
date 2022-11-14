from django.urls import path

from . import views

app_name = 'metal'
urlpatterns = [
    path('', views.MetalTopView.as_view(), name='index'),
    path('buy/', views.MetalBuy.as_view(), name='buy'),
    path('api/info/', views.MetalAllInfoAPI.as_view(), name='allinfo'),
    path('api/info/buy/', views.MetalBuyAPI, name='buyapi'),
    path('api/info/<str:type_name>/', views.MetalInfoAPI.as_view(), name='info'),
]
