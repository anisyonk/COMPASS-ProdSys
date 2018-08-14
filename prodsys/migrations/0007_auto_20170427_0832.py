# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodsys', '0006_auto_20170426_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='period',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='slot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.IntegerField(choices=[(10, 'test production'), (20, 'mass production')], default=10),
        ),
    ]