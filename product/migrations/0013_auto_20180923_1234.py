# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-23 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20180827_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=models.ImageField(default='media_cdn/protected_media/products/no-ig.jpg', upload_to='media_cdn/protected_media/products/'),
        ),
    ]
