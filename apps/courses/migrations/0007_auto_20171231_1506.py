# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_lesson_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(default='', max_length=200, verbose_name='访问地址'),
        ),
    ]
