# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-24 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20160109_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='bank_account_number',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Bank account number'),
        ),
    ]
