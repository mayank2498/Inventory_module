# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-07 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0021_auto_20170707_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='units',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
    ]