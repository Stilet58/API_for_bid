# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api_organization', '0008_auto_20170912_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='date_of_dispatch',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата и время отправки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='credit_organization',
            name='phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='end_date_of_rotation',
            field=models.DateTimeField(blank=True, verbose_name='Дата и время окончания ротации'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='start_date_of_rotation',
            field=models.DateTimeField(blank=True, verbose_name='Дата и время начала ротации'),
        ),
    ]
