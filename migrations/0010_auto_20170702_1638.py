# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-02 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_stock_subcategory_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='measured_unit',
            field=models.CharField(default='Kg', max_length=500, null=True),
        ),
    ]
