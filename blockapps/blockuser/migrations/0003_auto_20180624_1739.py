# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockuser', '0002_auto_20180624_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockuser',
            name='tel',
            field=models.CharField(blank=True, max_length=30, verbose_name='telphone number'),
        ),
    ]
