# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20171229_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='url',
            field=models.CharField(default='', max_length=200, verbose_name='访问地址'),
        ),
    ]