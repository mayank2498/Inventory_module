# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-07 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_auto_20170707_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='name',
            field=models.CharField(default='NoName', max_length=500),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='unit',
            field=models.CharField(default='Kg', max_length=100),
        ),
    ]
