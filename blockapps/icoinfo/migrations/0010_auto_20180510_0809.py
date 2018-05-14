# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 08:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('icoinfo', '0009_auto_20180508_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='IcoBasicInfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ico_name', models.CharField(default='', max_length=255, verbose_name='项目名称')),
                ('token', models.CharField(default='', max_length=255, verbose_name='项目代号')),
                ('category', models.CharField(default='', max_length=255, verbose_name='类别（可挖不可挖矿平台币应用币）')),
                ('first_block_time', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=utc), verbose_name='第一个区块生成时间')),
                ('ico_price', models.CharField(default='', max_length=255, verbose_name='ico价格')),
                ('total_volumn', models.BigIntegerField(default=0, verbose_name='币总量')),
                ('maximum_tps', models.CharField(default='', max_length=255, verbose_name='最大每秒传输量')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'managed': True,
                'abstract': False,
                'verbose_name': 'ico基本信息表',
                'db_table': 'ico_basic_info',
            },
        ),
        migrations.RemoveField(
            model_name='icostatsmodel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='icostatsmodel',
            name='first_block_time',
        ),
        migrations.RemoveField(
            model_name='icostatsmodel',
            name='ico_price',
        ),
        migrations.RemoveField(
            model_name='icostatsmodel',
            name='maximum_tps',
        ),
        migrations.RemoveField(
            model_name='icostatsmodel',
            name='total_volumn',
        ),
        migrations.AddField(
            model_name='icostatsmodel',
            name='per_transactions_volume',
            field=models.CharField(default='', max_length=255, verbose_name='矿工收入/交易量'),
        ),
    ]