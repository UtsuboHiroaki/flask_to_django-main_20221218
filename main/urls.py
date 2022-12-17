from django.http import HttpResponse
from django.urls import path

from .views import base_views, sample_views, sample_class_views, error_views


def sample01_func(request):
    return HttpResponse('<h1>sample1_funcに呼ばれました！</h1>')


app_name = 'main'

urlpatterns = [
    path('', base_views.TopView.as_view(), name='index'),
    path('about/', base_views.AbountView.as_view(), name='about'),
    path('reference/', base_views.ReferenceView.as_view(), name='reference'),
    path('buy_thanks/', base_views.ThanksView.as_view(), name='thanks'),

    path('sample01/', sample01_func, name='sample01'),
    path('sample11/', sample_views.SampleClass11(), name='sample11'),
    path('sample12/', sample_views.SampleClass12().my_method, name='sample12'),
    path('sample13/', sample_views.func_13, name='sample13'),
    path('sample21/', sample_class_views.func_21, name='sample21'),
    path('sample22/', sample_class_views.func_22, name='sample22'),
    path('sample23/', sample_class_views.func_23, name='sample23'),

    path('normal_403/', error_views.normal_403, name='normal_403'),
    path('normal_403_class/', error_views.normal_403_class, name='normal_403_class'),
    path('raise_403/', error_views.raise_403, name='raise_403'),

    path('normal_400/', error_views.normal_400, name='normal_400'),
    path('normal_400_class/', error_views.normal_400_class, name='normal_400_class'),
    path('raise_400/', error_views.raise_400, name='raise_400'),

    path('raise_500/', error_views.raise_500, name='raise_500'),
]
