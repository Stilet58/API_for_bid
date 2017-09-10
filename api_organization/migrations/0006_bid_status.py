# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_organization', '0005_remove_bid_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='status',
            field=models.CharField(choices=[('new', 'Новая'), ('sent', 'Отправлена'), ('recieved', 'Получена')], default='Новая', max_length=50, verbose_name='Статус'),
        ),
    ]
