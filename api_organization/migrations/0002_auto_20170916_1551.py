# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-16 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='credit_organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_organization.Credit_organization', verbose_name='Кредитная организация'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='type_of_a_proposal',
            field=models.CharField(choices=[('consumer', 'Потребительский кредит'), ('hypothec', 'Ипотека'), ('auto_loan', 'Автокредит'), ('kmsb', 'КМСБ')], max_length=100, verbose_name='Тип'),
        ),
    ]
