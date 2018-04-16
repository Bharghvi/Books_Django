# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import orders
# Register your models here.

class ordersAdmin(admin.ModelAdmin):
    class Meta:
        model = orders

admin.site.register(orders, ordersAdmin)
