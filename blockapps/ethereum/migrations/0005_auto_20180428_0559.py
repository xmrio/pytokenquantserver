# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-28 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ethereum', '0004_auto_20180428_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ethereumtransactionmodel',
            name='input_data',
            field=models.TextField(default='', verbose_name='交易发送的数据'),
        ),
    ]