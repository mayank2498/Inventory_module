# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-30 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20170630_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
