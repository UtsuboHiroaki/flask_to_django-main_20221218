from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.TopView.as_view(), name='index'),
    path('about/', views.AbountView.as_view(), name='about'),
    path('reference/', views.ReferenceView.as_view(), name='reference'),
    path('buy_thanks/', views.ThanksView.as_view(), name='thanks'),
]
