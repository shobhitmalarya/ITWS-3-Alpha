# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 17:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='soil_moisture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_level', models.FloatField(default=0.0)),
                ('dt', models.DateTimeField(default=datetime.datetime(2017, 10, 5, 22, 31, 38, 576871))),
            ],
        ),
        migrations.CreateModel(
            name='water_level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.FloatField(default=0.0)),
                ('is_on', models.CharField(choices=[('1', 'YES'), ('0', 'OFF')], max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='temp_read',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 5, 22, 31, 38, 575868)),
        ),
        migrations.AlterField(
            model_name='temp_read',
            name='temp',
            field=models.FloatField(default=0.0),
        ),
    ]
