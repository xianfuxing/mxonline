# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20171203_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='logo'),
        ),
    ]
