# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_promocode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='product_item',
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together=set([('latitude', 'longitude')]),
        ),
    ]
