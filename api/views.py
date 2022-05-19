from django.http import JsonResponse
from api.models import *


def GivingData(request):
    data = list(Giving.objects.values())
    return JsonResponse(data, safe=False)


def LinkData(request):
    data = list(Link.objects.values())
    return JsonResponse(data, safe=False)


def ServiceData(request):
    data = list(Service.objects.values())
    return JsonResponse(data, safe=False)


def SmallGroupData(request):
    data = list(SmallGroup.objects.values())
    return JsonResponse(data, safe=False)


def StaffData(request):
    data = list(Staff.objects.order_by('view_order').values())
    for i, d in enumerate(data):
        data[i]['image'] = d['image'].url
    return JsonResponse(data, safe=False)
