# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-01 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20170701_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='subcategory_id',
            field=models.IntegerField(default=0),
        ),
    ]
