# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-07 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_purchase_cost_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]