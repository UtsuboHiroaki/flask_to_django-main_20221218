from pathlib import Path

import markdown
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
class TopView(TemplateView):
    """トップページ"""
    template_name = "index.html"


class AbountView(TemplateView):
    """このサイトについて"""
    template_name = "about.html"


class ReferenceView(View):
    """参考文献"""

    def get(self, request, *args, **kwargs):
        readmd_str = Path(__file__).parent.parent.joinpath('templates', 'reference.md').read_text(encoding='utf-8')
        note = markdown.markdown(readmd_str,
                                 extensions=['markdown.extensions.tables', 'markdown.extensions.fenced_code', ])
        context = {
            "note": note,
        }
        return render(request, 'reference.html', context)


class ThanksView(TemplateView):
    """このサイトについて"""
    template_name = "buy_thanks.html"
