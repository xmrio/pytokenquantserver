# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-30 06:26
from __future__ import unicode_literals

from django.db import migrations
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blockuser', '0006_auto_20180819_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duiqiaopolicy',
            name='secretkey',
            field=encrypted_fields.fields.EncryptedTextField(help_text='请填写您在交易所的api secret key', verbose_name='SecretKey'),
        ),
    ]
