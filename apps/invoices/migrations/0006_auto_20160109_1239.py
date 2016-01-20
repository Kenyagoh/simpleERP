# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 12:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0005_auto_20160109_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceposition',
            name='money_gross',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=32, verbose_name='Price gross'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceposition',
            name='money_net',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=32, verbose_name='Price net'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceposition',
            name='tax',
            field=models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=10, verbose_name='Price gross'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_delivered',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Delivery date'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_issued',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Issue date'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_payment',
            field=models.DateField(blank=True, help_text='If you leave this field blank, it will be filled in automatically.', null=True, verbose_name='Payment date'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(blank=True, help_text='If you leave this field blank, it will be filled in automatically.', max_length=128, verbose_name='Invoice number'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.IntegerField(blank=True, help_text='If you leave this field blank, it will be filled in automatically.', verbose_name='Invoice internal number'),
        ),
    ]