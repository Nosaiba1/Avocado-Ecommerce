# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-27 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20180808_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_favourite_value',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
