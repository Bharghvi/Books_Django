# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from books.models import books
from .models import orders
# Create your views here.

def cart(request):
    data = books.objects.all();
    total = 0
    for val in data:
        if val.atc == 'Y':
            total += (val.price - (val.price*0.01*val.discount))
    context = {'data': data, 'total': total}
    template = 'cart.html'
    return render(request, template, context)

def payment(request):
    from django.http import JsonResponse
    if request.method=='POST' and request.is_ajax():
        try:
            obj = books.objects.all()
            for val in obj:
                if val.atc == 'Y':
                    val.atc = 'N'
                    val.save()
            payment = request.POST['payment']
            total = request.POST['total']
            address = request.POST['address']
            p = orders(payment=payment, address=address, total=str(total))
            p.save()
            return JsonResponse({'total':total, 'msg': payment})
        except books.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})


def cartRemove(request):
    from django.http import JsonResponse
    if request.method=='POST' and request.is_ajax():
        try:
            id = request.POST['id']
            obj = books.objects.get(bid=id)
            obj.atc = 'N'
            obj.save()
            return JsonResponse({'status':'Success', 'msg': 'save successfully'})
        except books.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})
    # else:
    #     return JsonResponse({'status':'Fail', 'msg':'Not a valid request'}
