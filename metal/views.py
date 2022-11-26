import json

from django.contrib import messages
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import MetalType, MetalPurchase


def metal_top_view(request):
    prices = MetalType.objects.all()
    return render(request, 'metal/index.html', context={'prices': prices}, )


def metal_buy_view(request):
    if request.method == 'GET':
        items = MetalType.objects.all()
        context = {"items": items}
        return render(request, 'metal/buy.html', context)
    elif request.method == 'POST':
        metal_type = request.POST['metal_type']
        try:
            metal = MetalType.objects.get(metal_type=metal_type)
        except MetalType.DoesNotExist:
            messages.warning(request, f'Metal type does not exist: {metal_type}')
            return HttpResponseRedirect(reverse('metal:func_buy'))
        weight = request.POST['weight']
        email = request.POST['email']
        name = request.POST['name']

        purchase = MetalPurchase(metal_type=metal, weight=weight, email=email, name=name)
        purchase.save()

        messages.success(request, '毎度ありがとうございます！')
        return HttpResponseRedirect(reverse('main:thanks'))


# Create your views here.
class MetalTopView(View):
    """トップページ"""

    def get(self, request, *args, **kwargs):
        prices = MetalType.objects.all()
        context = {'prices': prices}
        return render(request, 'metal/index.html', context)


class MetalBuy(View):
    """
    貴金属買取ページ
    """

    def get(self, request, *args, **kwargs):
        items = MetalType.objects.all()
        context = {"items": items}
        return render(request, 'metal/buy.html', context)

    def post(self, request, *args, **kwargs):
        metal_type = request.POST['metal_type']
        metal_type = MetalType.objects.get(metal_type=metal_type)
        weight = request.POST['weight']
        email = request.POST['email']
        name = request.POST['name']

        purchase = MetalPurchase(metal_type=metal_type, weight=weight, email=email, name=name)
        purchase.save()

        return HttpResponseRedirect(reverse('main:thanks'))


class MetalInfoAPI(View):
    """
    貴金属の情報を返す
    :param type_name:対象となる金属の名前
    :return:
    """

    def get(self, request, type_name, *args, **kwargs):
        exist = MetalType.objects.filter(metal_type=type_name)
        if not exist:
            data = {'error': '受け付けられません。当店では扱っていない貴金属です。'}
            dump_params = {
                "ensure_ascii": False
            }
            return JsonResponse(data, json_dumps_params=dump_params, status=404)
        metal = MetalType.objects.get(metal_type=type_name)
        data = {
            'id': metal.id,
            'metal_type': metal.metal_type,
            'buy': metal.buy,
            'sell': metal.sell,
        }
        return JsonResponse(data)


class MetalAllInfoAPI(View):
    """
    全ての貴金属の情報を返す
    """

    def get(self, request, *args, **kwargs):
        metals = MetalType.objects.all()
        result_dict = {}
        for metal in metals:
            result_dict[metal.id] = {'id': metal.id, 'metal_type': metal.metal_type, 'buy': metal.buy,
                                     'sell': metal.sell, }

        return JsonResponse(result_dict)


@csrf_exempt
def MetalBuyAPI(request):
    if request.method == 'GET':
        dump_params = {
            "ensure_ascii": False
        }
        return JsonResponse({'error': 'POSTメソッドのみ受け付けています。'}, json_dumps_params=dump_params, status=404)
    data = json.loads(request.body)
    exist = MetalType.objects.filter(metal_type=data['name'])
    if not exist:
        dump_params = {
            "ensure_ascii": False
        }
        data = {'error': '受け付けられません。当店では扱っていない貴金属です。'}
        return JsonResponse(data, json_dumps_params=dump_params, status=404)

    metal_type = MetalType.objects.get(metal_type=data['name'])
    weight = data['amount']
    email = data['email']
    name = data['user']

    purchase = MetalPurchase(metal_type=metal_type, weight=weight, email=email, name=name)
    purchase.save()

    data = {
        'result': 'success',
        'price': metal_type.buy * weight
    }
    return JsonResponse(data)

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
#         exist = MetalType.objects.filter(metal_type=metal_type)
#         if not exist:
#             dump_params = {
#                 "ensure_ascii": False
#             }
#             data = {'error': '受け付けられません。当店では扱っていない貴金属です。'}
#             return JsonResponse(data, json_dumps_params=dump_params, status=404)
#
#         metal_type = MetalType.objects.get(metal_type=metal_type)
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
