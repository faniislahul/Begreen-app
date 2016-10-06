# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20160902_0016'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='p_bbtl',
            new_name='p_bb',
        ),
        migrations.RemoveField(
            model_name='p_bbl',
            name='bb',
        ),
        migrations.RemoveField(
            model_name='p_bbl',
            name='produk',
        ),
        migrations.AddField(
            model_name='bahan_baku',
            name='langsung',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='p_bbl',
        ),
    ]