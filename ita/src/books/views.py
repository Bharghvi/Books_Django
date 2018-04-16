# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import books
# Create your views here.

def bookss(request):
    data = books.objects.all();
    context = {'data': data}
    template = 'books.html'
    return render(request, template, context)

def cartChange(request):
    from django.http import JsonResponse
    if request.method=='POST' and request.is_ajax():
        try:
            id = request.POST['id']
            obj = books.objects.get(bid=id)
            if obj.atc == 'N':
                obj.atc = 'Y'
            else:
                obj.atc = 'N'
            obj.save()
            return JsonResponse({'status':'Success', 'msg': 'save successfully'})
        except books.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})
    # else:
    #     return JsonResponse({'status':'Fail', 'msg':'Not a valid request'}

def related(request):
    from django.http import JsonResponse
    if request.method=='POST' and request.is_ajax():
        try:
            id = request.POST['id']
            obj = books.objects.get(bid=id)
            more = obj.desciption
            return JsonResponse({'status':'Success', 'msg': more})
        except books.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})
    # else:
    #     return JsonResponse({'status':'Fail', 'msg':'Not a valid request'}
