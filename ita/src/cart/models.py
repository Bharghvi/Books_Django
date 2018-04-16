# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class orders(models.Model):
    payment = models.CharField(blank=False, null=False, max_length=80)
    address = models.TextField(max_length=150, blank=False, null=False)
    total = models.CharField(max_length=10, null=False, blank=False)

    def __unicode__(self):
        return self.payment
