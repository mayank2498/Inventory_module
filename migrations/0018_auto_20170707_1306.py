# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-07 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_auto_20170707_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='cost_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
