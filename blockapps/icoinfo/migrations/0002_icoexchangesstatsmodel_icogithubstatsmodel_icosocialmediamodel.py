# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 10:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('icoinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IcoExchangesStatsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ico_name', models.CharField(default='', max_length=255, verbose_name='项目名称')),
                ('token', models.CharField(default='', max_length=255, verbose_name='项目代号')),
                ('fair_price', models.DecimalField(decimal_places=5, default=0, max_digits=40, verbose_name='公允价格')),
                ('change_24h', models.DecimalField(decimal_places=5, default=0, max_digits=40, verbose_name='24小时变化百分比')),
                ('circulating_supply', models.BigIntegerField(default=0, verbose_name='已供应币数')),
                ('max_supply', models.BigIntegerField(default=0, verbose_name='总供应币数')),
                ('market_capitalization', models.DecimalField(decimal_places=5, default=0, max_digits=40, verbose_name='市值')),
                ('transactions_last_24h', models.BigIntegerField(default=0, verbose_name='24小时交易量')),
                ('total_trade_volume_24h', models.DecimalField(decimal_places=5, default=0, max_digits=40, verbose_name='24小时交易所成交总额')),
                ('turnover_rate', models.DecimalField(decimal_places=5, default=0, max_digits=40, verbose_name='换手率')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='记录创建时间')),
            ],
            options={
                'verbose_name': 'ico交易所统计表',
                'db_table': 'ico_exchanges_stats',
                'abstract': False,
                'managed': True,
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
        migrations.CreateModel(
            name='IcoGithubStatsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ico_name', models.CharField(default='', max_length=255, verbose_name='项目名称')),
                ('token', models.CharField(default='', max_length=255, verbose_name='项目代号')),
                ('release', models.CharField(default='', max_length=255, verbose_name='版本信息')),
                ('stars', models.IntegerField(default=0, verbose_name='stars个数')),
                ('stars_incr_week', models.IntegerField(default=0, verbose_name='本周新增星数')),
                ('commits_this_month', models.IntegerField(default=0, verbose_name='近一个月提交次数')),
                ('commits_last_week', models.IntegerField(default=0, verbose_name='上周提交次数')),
                ('commits_this_week', models.IntegerField(default=0, verbose_name='本周提交次数')),
                ('codes_this_month', models.IntegerField(default=0, verbose_name='近一个月代码提交量')),
                ('codes_last_week', models.IntegerField(default=0, verbose_name='上周代码提交量')),
                ('codes_this_week', models.IntegerField(default=0, verbose_name='本周代码提交量')),
                ('branches', models.IntegerField(default=0, verbose_name='分支数')),
                ('issues', models.IntegerField(default=0, verbose_name='问题数')),
                ('watchers', models.IntegerField(default=0, verbose_name='关注数')),
                ('projects', models.TextField(default='', verbose_name='项目库')),
                ('project_create_time', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=utc), verbose_name='项目创建时间')),
                ('project_update_time', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=utc), verbose_name='最后提交时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='记录创建时间')),
            ],
            options={
                'verbose_name': 'github统计表',
                'db_table': 'ico_github_stats',
                'abstract': False,
                'managed': True,
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
        migrations.CreateModel(
            name='IcoSocialMediaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ico_name', models.CharField(default='', max_length=255, verbose_name='项目名称')),
                ('token', models.CharField(default='', max_length=255, verbose_name='项目代号')),
                ('reddit_subscribers', models.IntegerField(default=0, verbose_name='reddit订阅数')),
                ('twitter_followers', models.IntegerField(default=0, verbose_name='twitter订阅数')),
                ('twitter_per_day', models.IntegerField(default=0, verbose_name='每日推文数')),
                ('weibo_post', models.IntegerField(default=0, verbose_name='微博数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='记录创建时间')),
            ],
            options={
                'verbose_name': '社交媒体指标表',
                'db_table': 'ico_social_medial',
                'abstract': False,
                'managed': True,
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
    ]
