# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_promocode_code_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=models.ImageField(default='media_cdn/protected_media/products/no-ig.jpg', upload_to='products'),
        ),
    ]
