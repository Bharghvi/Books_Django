# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-14 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='desciption',
            field=models.TextField(default='description default text'),
        ),
    ]