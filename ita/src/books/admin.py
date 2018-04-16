# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import books
# Register your models here.

class booksAdmin(admin.ModelAdmin):
    class Meta:
        model = books

admin.site.register(books, booksAdmin)
