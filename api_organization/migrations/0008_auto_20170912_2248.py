# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api_organization', '0007_delete_status_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit_organization',
            name='date_of_change',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения'),
        ),
        migrations.AddField(
            model_name='credit_organization',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата и время создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bid',
            name='date_of_dispatch',
            field=models.DateTimeField(null=True, verbose_name='Дата и время отправки'),
        ),
    ]
