# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20180807_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.FloatField(default=0),
        ),
    ]
