# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY;
# Create your views here.
@login_required
def checkout(request):
    from django.http import JsonResponse
    if request.method=='POST':
        try:
            name = request.POST['pay']
            pm = 'N'
            if name == 'cash':
                pm = 'Y'
            print pm
            return JsonResponse({'status':'Success', 'msg': 'save successfully'})
        except:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})
    context = {'pay' : pay}
    template = 'checkout.html'
    return render(request, template, context)
