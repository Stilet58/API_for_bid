# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-16 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_partners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('sent', 'Отправлена'), ('recieved', 'Получена')], default='Новая', max_length=50, verbose_name='Статус')),
                ('date_of_dispatch', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время отправки')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_partners.Form', verbose_name='Анкета')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Credit_organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('date_of_change', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Кредитная организация',
                'verbose_name_plural': 'Кредитные организации',
            },
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('date_of_change', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('name', models.CharField(max_length=250, verbose_name='Название предложения')),
                ('type_of_a_proposal', models.CharField(max_length=100, verbose_name='Тип')),
                ('min_scoring_ball', models.IntegerField(verbose_name='Минимальный скоринговый балл')),
                ('max_scoring_ball', models.IntegerField(verbose_name='Максимальный скоринговый балл')),
                ('start_date_of_rotation', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время начала ротации')),
                ('end_date_of_rotation', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время окончания ротации')),
                ('credit_organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_organization.Credit_organization', verbose_name='Кредитная организация')),
            ],
            options={
                'verbose_name': 'Предложение',
                'verbose_name_plural': 'Предложения',
            },
        ),
        migrations.AddField(
            model_name='bid',
            name='proposal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_organization.Proposal', verbose_name='Предложение'),
        ),
    ]
