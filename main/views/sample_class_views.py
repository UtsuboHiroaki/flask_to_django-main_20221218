from django.http import HttpResponse
from django.views.generic import View, TemplateView


class SampleClass21(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1>SampleClass21に呼ばれました！</h1>')


func_21 = SampleClass21.as_view()


class SampleClass22(TemplateView):
    template_name = "sample_without_context.html"


func_22 = SampleClass22.as_view()


class SampleClass23(TemplateView):
    template_name = "sample_with_context.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'メッセージです'
        return context


func_23 = SampleClass23.as_view()
