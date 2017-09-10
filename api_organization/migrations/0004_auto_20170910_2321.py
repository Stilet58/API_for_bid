# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_organization', '0003_auto_20170910_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_partners.Form'),
        ),
        migrations.DeleteModel(
            name='Form',
        ),
    ]
