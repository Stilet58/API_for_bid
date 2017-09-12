# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_organization', '0011_auto_20170912_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='credit_organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_organization.Credit_organization', verbose_name='Кредитная организация'),
        ),
    ]