# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-28 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ethereum', '0002_auto_20180427_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ethereumblockmodel',
            name='nonce',
            field=models.CharField(default=0, max_length=255, verbose_name='随机数'),
        ),
    ]