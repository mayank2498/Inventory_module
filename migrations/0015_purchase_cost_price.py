# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-07 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20170707_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='cost_price',
            field=models.IntegerField(default=0),
        ),
    ]
