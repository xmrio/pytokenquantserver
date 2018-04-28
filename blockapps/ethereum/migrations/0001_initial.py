# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-27 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EthereumAddressModel',
            fields=[
                ('address', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('received', models.BigIntegerField(default=0, verbose_name='总接收数量')),
                ('sent', models.BigIntegerField(default=0, verbose_name='总支出数量')),
                ('balance', models.BigIntegerField(default=0, verbose_name='当前余额')),
                ('tx_count', models.BigIntegerField(default=0, verbose_name='交易数量')),
                ('unconfirmed_tx_count', models.BigIntegerField(default=0, verbose_name='未确认交易数量')),
                ('unconfirmed_rx_count', models.BigIntegerField(default=0, verbose_name='未确认总接收')),
                ('unconfirmed_sent', models.BigIntegerField(default=0, verbose_name='未确认总支出')),
                ('unspent_tx_count', models.BigIntegerField(default=0, verbose_name='未花费交易数量')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='记录创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
            ],
            options={
                'managed': True,
                'verbose_name': '以太坊地址余额表',
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'db_table': 'ethereum_address',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EthereumBlockModel',
            fields=[
                ('number', models.BigIntegerField(primary_key=True, serialize=False)),
                ('hash', models.CharField(default='', max_length=255, verbose_name='区块哈希')),
                ('parent_hash', models.CharField(default='', max_length=255, verbose_name='父哈希')),
                ('nonce', models.BigIntegerField(default=0, verbose_name='随机数')),
                ('transactions_root', models.CharField(default='', max_length=255, verbose_name='根交易字典树')),
                ('state_root', models.CharField(default='', max_length=255, verbose_name='根状态字典树')),
                ('receipts_root', models.CharField(default='', max_length=255, verbose_name='根收据字典树')),
                ('miner', models.CharField(default='', max_length=255, verbose_name='矿工')),
                ('difficulty', models.BigIntegerField(default=0, verbose_name='该区块难度')),
                ('total_difficulty', models.BigIntegerField(default=0, verbose_name='区块累计总难度')),
                ('extra_data', models.CharField(default='', max_length=255, verbose_name='区块额外信息')),
                ('size', models.BigIntegerField(default=0, verbose_name='区块字节数')),
                ('gas_limit', models.BigIntegerField(default=0, verbose_name='gas上限')),
                ('gas_used', models.BigIntegerField(default=0, verbose_name='该区块gas使用总量')),
                ('timestamp', models.BigIntegerField(default=0, verbose_name='区块创建时间戳')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='记录创建时间')),
            ],
            options={
                'managed': True,
                'verbose_name': '以太坊区块表',
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'db_table': 'ethereum_block',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EthereumStatsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocks_last_24h', models.BigIntegerField(default=0, verbose_name='24小时生成区块数')),
                ('blocks_avg_perhour', models.BigIntegerField(default=0, verbose_name='每小时生成区块数')),
                ('reward_last_24h', models.BigIntegerField(default=0, verbose_name='24小时产生奖励数')),
                ('top_100_richest', models.BigIntegerField(default=0, verbose_name='前100占有币情况')),
                ('wealth_distribution_top10', models.BigIntegerField(default=0, verbose_name='财富10')),
                ('wealth_distribution_top100', models.BigIntegerField(default=0, verbose_name='财富100')),
                ('wealth_distribution_top1000', models.BigIntegerField(default=0, verbose_name='财富1000')),
                ('wealth_distribution_top10000', models.BigIntegerField(default=0, verbose_name='财富10000')),
                ('address_richer_than_1usd', models.BigIntegerField(default=0, verbose_name='金额超过1usd地址')),
                ('address_richer_than_100usd', models.BigIntegerField(default=0, verbose_name='金额超过100usd地址')),
                ('address_richer_than_1000usd', models.BigIntegerField(default=0, verbose_name='金额超过1000usd地址')),
                ('address_richer_than_10000usd', models.BigIntegerField(default=0, verbose_name='金额超过10000usd地址')),
                ('active_addresses_last24h', models.BigIntegerField(default=0, verbose_name='24小时活跃地址数')),
                ('transaction_largest100', models.BigIntegerField(default=0, verbose_name='24小时最大100笔交易')),
                ('address_numbers', models.BigIntegerField(default=0, verbose_name='持币地址数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='记录创建时间')),
                ('total', models.BigIntegerField(default=0, verbose_name='币总量')),
            ],
            options={
                'managed': True,
                'verbose_name': '以太坊指标表',
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'db_table': 'ethereum_stats',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EthereumTransactionModel',
            fields=[
                ('txhash', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='交易哈希')),
                ('nonce', models.BigIntegerField(default=0, verbose_name='随机数')),
                ('block_hash', models.CharField(default='', max_length=255, verbose_name='区块哈希')),
                ('block_number', models.BigIntegerField(default=0, verbose_name='区块高度')),
                ('txindex', models.BigIntegerField(default=0, verbose_name='交易序号')),
                ('from_address', models.CharField(default='', max_length=255, verbose_name='发送方地址')),
                ('to_address', models.CharField(default='', max_length=255, verbose_name='接收方地址')),
                ('value', models.BigIntegerField(default=0, verbose_name='交易金额Wei')),
                ('gas_price', models.BigIntegerField(default=0, verbose_name='gas价格')),
                ('gas', models.BigIntegerField(default=0, verbose_name='gas数量')),
                ('input_data', models.CharField(default='', max_length=255, verbose_name='交易发送的数据')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='记录创建时间')),
            ],
            options={
                'managed': True,
                'verbose_name': '以太坊交易记录表',
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'db_table': 'ethereum_transaction',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EthereumTransactionReceiptModel',
            fields=[
                ('txhash', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='交易哈希')),
                ('txindex', models.BigIntegerField(default=0, verbose_name='交易序号')),
                ('block_hash', models.CharField(default='', max_length=255, verbose_name='区块哈希')),
                ('block_number', models.BigIntegerField(default=0, verbose_name='区块高度')),
                ('total_gas', models.BigIntegerField(default=0, verbose_name='区块gas使用总量')),
                ('gas', models.BigIntegerField(default=0, verbose_name='该交易使用gas量')),
                ('contract_address', models.CharField(default='', max_length=255, verbose_name='合约地址')),
                ('root', models.CharField(default='', max_length=255, verbose_name='拜占庭交易状态根')),
                ('status', models.BigIntegerField(default=0, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='记录创建时间')),
            ],
            options={
                'managed': True,
                'verbose_name': '以太坊交易收据表',
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'db_table': 'ethereum_transaction_receipt',
                'abstract': False,
            },
        ),
    ]