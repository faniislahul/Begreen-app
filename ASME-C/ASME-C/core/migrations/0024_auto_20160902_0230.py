# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_produk_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='kode',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
