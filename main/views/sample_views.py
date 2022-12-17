"""
path生成時の第二引数は、カラブルでさえあればよい
(ただし、 __init__ メソッドは戻り値を返さないので使えないが)
"""
from django.http import HttpResponse


# クラスインスタンスでもOK
class SampleClass11:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, request):
        return HttpResponse('<h1>SampleClass11に呼ばれました！</h1>')


# インスタンスメソッドでもOK
class SampleClass12:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def my_method(self, request):
        return HttpResponse('<h1>SampleClass12に呼ばれました！</h1>')


class SampleClass13:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, request):
        return HttpResponse('<h1>SampleClass13に呼ばれました！</h1>')


func_13 = SampleClass13()
