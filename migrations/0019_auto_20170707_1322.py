# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-07 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_auto_20170707_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
