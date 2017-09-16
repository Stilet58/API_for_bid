# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-16 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('date_of_change', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('surname', models.CharField(default='', max_length=200, verbose_name='Фамилия')),
                ('first_name', models.CharField(default='', max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(default='', max_length=200, verbose_name='Отчество')),
                ('dob', models.DateField(verbose_name='Дата рождения')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Телефон')),
                ('phone_confirmation', models.CharField(choices=[('Yes', 'Да'), ('No', 'Нет')], default='Нет', max_length=5, verbose_name='Телефон подтвержден')),
                ('passport', models.CharField(max_length=100, verbose_name='Паспорт')),
                ('scoring_ball', models.IntegerField(blank=True, null=True, verbose_name='Скоринговый балл')),
            ],
            options={
                'verbose_name': 'Анкета клиента',
                'verbose_name_plural': 'Анкеты клиента',
            },
        ),
    ]