from django.core.exceptions import PermissionDenied, BadRequest
from django.http import HttpResponseForbidden, HttpResponse
from django.utils import timezone


def normal_403(request):
    time_limit = timezone.now() + timezone.timedelta(minutes=-30)
    if time_limit < timezone.now():
        return HttpResponse('<h1>このページに来たのが遅すぎです</h1>', status=403)


def normal_403_class(request):
    time_limit = timezone.now() + timezone.timedelta(minutes=30)
    if time_limit > timezone.now():
        return HttpResponseForbidden('<h1>このページに来たのが遅すぎです</h1>')


def raise_403(request):
    time_limit = timezone.now() + timezone.timedelta(minutes=30)
    if not time_limit == timezone.now():
        raise PermissionDenied('<h1>このページに来るタイミングはきっかりでなくてはなりません</h1>')


def normal_400(request):
    return HttpResponse('<h1>400エラーです</h1>', status=400)


def normal_400_class(request):
    return HttpResponseForbidden('<h1>400エラーです</h1>')


def raise_400(request):
    raise BadRequest('不審なリクエストなので400エラーです。')


def raise_500(request):
    raise Exception('<h1>500エラーです</h1>')
