# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 21:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_partners', '0006_auto_20170912_2312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='form',
            options={'verbose_name': 'Анкета клиента', 'verbose_name_plural': 'Анкет клиента'},
        ),
    ]