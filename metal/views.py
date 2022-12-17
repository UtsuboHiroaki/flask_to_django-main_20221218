import json

from django.contrib import messages
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from .models import Metal, MetalPurchase


def redirect_func(request):
    """ 関数ベースビューのリダイレクト例 """
    return HttpResponseRedirect(resolve_url('metal:index'))


def metal_top_view(request):
    metals = Metal.objects.all()
    return render(request, 'metal/index.html', context={'metals': metals}, )


def metal_buy_view(request):
    if request.method == 'GET':
        metals = Metal.objects.all()
        context = {"metals": metals}
        return render(request, 'metal/buy.html', context)
    elif request.method == 'POST':
        metal_name = request.POST['metal_name']
        try:
            metal = Metal.objects.get(name=metal_name)
        except Metal.DoesNotExist:
            messages.warning(request, f'Metal type does not exist: {metal_name}')
            return HttpResponseRedirect(reverse('metal:func_buy'))
        weight = request.POST['weight']
        email = request.POST['email']
        name = request.POST['name']

        purchase = MetalPurchase(metal=metal, weight=weight, email=email, name=name)
        purchase.save()

        messages.success(request, '毎度ありがとうございます！')
        return HttpResponseRedirect(reverse('main:thanks'))


# Create your views here.
class MetalTopView(View):
    """トップページ"""

    def get(self, request, *args, **kwargs):
        metals = Metal.objects.all()
        context = {'metals': metals}
        return render(request, 'metal/index.html', context)


class MetalDetail(DetailView):
    """詳細ページ"""

    model = Metal
    template_name = 'metal/detail.html'


class MetalBuy(View):
    """
    貴金属買取ページ
    """

    def get(self, request, *args, **kwargs):
        metals = Metal.objects.all()
        context = {"metals": metals}
        return render(request, 'metal/buy.html', context)

    def post(self, request, *args, **kwargs):
        metal_name = request.POST['metal_name']
        metal = Metal.objects.get(name=metal_name)
        weight = request.POST['weight']
        email = request.POST['email']
        name = request.POST['name']

        purchase = MetalPurchase(metal=metal, weight=weight, email=email, name=name)
        purchase.save()

        messages.success(request, '毎度ありがとうございます！')
        return HttpResponseRedirect(reverse('main:thanks'))


# 以下の api views については、 model の設計をいじったあとは動作未確認です。
class MetalInfoAPI(View):
    """
    貴金属の情報を返す
    :param type_name:対象となる金属の名前
    :return:
    """

    def get(self, request, type_name, *args, **kwargs):
        exist = Metal.objects.filter(name=type_name)
        if not exist:
            data = {'error': '受け付けられません。当店では扱っていない貴金属です。'}
            dump_params = {
                "ensure_ascii": False
            }
            return JsonResponse(data, json_dumps_params=dump_params, status=404)
        metal = Metal.objects.get(name=type_name)
        data = {
            'id': metal.id,
            'metal_type': metal.name,
            'buy': metal.buy,
            'sell': metal.sell,
        }
        return JsonResponse(data)


class MetalAllInfoAPI(View):
    """
    全ての貴金属の情報を返す
    """

    def get(self, request, *args, **kwargs):
        metals = Metal.objects.all()
        result_dict = {}
        for metal in metals:
            result_dict[metal.id] = {'id': metal.id, 'metal_type': metal.name, 'buy': metal.buy,
                                     'sell': metal.sell, }

        return JsonResponse(result_dict)


@csrf_exempt
def metal_buy_api(request):
    if request.method == 'GET':
        dump_params = {
            "ensure_ascii": False
        }
        return JsonResponse({'error': 'POSTメソッドのみ受け付けています。'}, json_dumps_params=dump_params, status=404)
    data = json.loads(request.body)
    exist = Metal.objects.filter(metal_type=data['name'])
    if not exist:
        dump_params = {
            "ensure_ascii": False
        }
        data = {'error': '受け付けられません。当店では扱っていない貴金属です。'}
        return JsonResponse(data, json_dumps_params=dump_params, status=404)

    metal = Metal.objects.get(metal_type=data['name'])
    weight = data['amount']
    email = data['email']
    name = data['user']

    purchase = MetalPurchase(metal=metal, weight=weight, email=email, name=name)
    purchase.save()

    data = {
        'result': 'success',
        'price': metal.buy * weight
    }
    return JsonResponse(data)


class MetalPurchaseList(View):
    """
    買取リストを表示する
    """

    def get(self, request, *args, **kwargs):
        purchase_list = MetalPurchase.objects.all().select_related('metal')
        context = {'purchase_list': purchase_list}
        return render(request, 'metal/purchase_list.html', context)

# class MetalBuyAPI(View):
#     """
#     貴金属買取API
#     """
#
#     def get(self, request, *args, **kwargs):
#         dump_params = {
#             "ensure_ascii": False
#         }
#         return JsonResponse({'error': 'POSTメソッドのみ受け付けています。'}, json_dumps_params=dump_params, status=404)
#
#     @method_decorator(ensure_csrf_cookie)
#     def post(self, request, *args, **kwargs):
#         metal_type = request.POST['metal_type']
#         exist = Metal.objects.filter(metal_type=metal_type)
#         if not exist:
#             dump_params = {
#                 "ensure_ascii": False
#             }
#             data = {'error': '受け付けられません。当店では扱っていない貴金属です。'}
#             return JsonResponse(data, json_dumps_params=dump_params, status=404)
#
#         metal_type = Metal.objects.get(metal_type=metal_type)
#         weight = request.POST['weight']
#         email = request.POST['email']
#         name = request.POST['name']
#
#         purchase = MetalPurchase(metal_type=metal_type, weight=weight, email=email, name=name)
#         purchase.save()
#
#         data = {
#             'result': 'success',
#             'price': metal_type.buy * weight
#         }
#         return JsonResponse(data)
