# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-23 07:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0022_auto_20170707_1818'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Purchase',
            new_name='PurchaseProduct',
        ),
    ]
