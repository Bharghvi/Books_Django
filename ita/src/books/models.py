# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class books(models.Model):
    bid = models.IntegerField(blank=False, null=False)
    name = models.CharField(blank=False, null=False, max_length=80)
    author = models.CharField(blank=False, null=False, max_length=50)
    image = models.CharField(max_length=150, blank=False, null=False)
    desciption = models.TextField(blank=True, null=False)
    price = models.IntegerField(blank=False, null=False)
    discount = models.IntegerField(blank=False, null=False)
    atc = models.CharField(null=False, blank=False, max_length=1)
    type = models.CharField(null=False, blank=False, max_length=20)

    def __unicode__(self):
        return self.name
