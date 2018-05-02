# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ethereum', '0007_auto_20180502_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ethereumaddressmodel',
            name='balance',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=40, verbose_name='当前余额'),
        ),
        migrations.AlterField(
            model_name='ethereumaddressmodel',
            name='received',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=40, verbose_name='总接收数量'),
        ),
        migrations.AlterField(
            model_name='ethereumaddressmodel',
            name='sent',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=40, verbose_name='总支出数量'),
        ),
        migrations.AlterField(
            model_name='ethereumblockmodel',
            name='difficulty',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=40, verbose_name='该区块难度'),
        ),
        migrations.AlterField(
            model_name='ethereumblockmodel',
            name='total_difficulty',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=40, verbose_name='区块累计总难度'),
        ),
        migrations.AlterField(
            model_name='ethereumtransactionmodel',
            name='gas_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=40, verbose_name='gas价格'),
        ),
        migrations.AlterField(
            model_name='ethereumtransactionmodel',
            name='value',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=40, verbose_name='交易金额Wei'),
        ),
        migrations.AlterField(
            model_name='ethereumtransactionreceiptmodel',
            name='gas_used',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=40, verbose_name='该交易使用gas量'),
        ),
        migrations.AlterField(
            model_name='ethereumtransactionreceiptmodel',
            name='total_gas',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=40, verbose_name='区块gas使用总量'),
        ),
    ]
