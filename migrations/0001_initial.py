# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-29 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_price', models.IntegerField(default=0)),
                ('purchased_units', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('purchased_product_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductSizeData')),
                ('purchased_product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductData')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(editable=False)),
                ('units', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductData')),
            ],
        ),
    ]
