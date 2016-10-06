# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20160818_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='cost_driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='p_bbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Bahan_baku')),
            ],
        ),
        migrations.CreateModel(
            name='p_bbtl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Bahan_baku')),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('kode', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('harga_jual', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='p_bbtl',
            name='produk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Produk'),
        ),
        migrations.AddField(
            model_name='p_bbl',
            name='produk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Produk'),
        ),
    ]