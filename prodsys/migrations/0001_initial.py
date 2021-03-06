# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt', models.IntegerField(default=1)),
                ('status', models.IntegerField(choices=[(10, 'defined'), (20, 'running'), (30, 'failed'), (40, 'paused'), (50, 'cancelled'), (60, 'merging'), (70, 'merged'), (80, 'x-checking'), (90, 'x-checked'), (100, 'done')], default=10)),
                ('run_number', models.IntegerField(default=0)),
                ('panda_id', models.BigIntegerField()),
                ('date_added', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('type', models.IntegerField(choices=[(10, 'prod'), (20, 'mc')], default=10)),
                ('path', models.CharField(default='', max_length=300)),
                ('soft', models.CharField(default='', max_length=300)),
                ('prodSlt', models.IntegerField(default=0)),
                ('phastVer', models.IntegerField(default=7)),
                ('template', models.CharField(default='template.opt', max_length=300)),
                ('filelist', models.TextField(null=True)),
                ('max_attempts', models.IntegerField(default=3)),
                ('status', models.IntegerField(choices=[(10, 'draft'), (20, 'ready'), (30, 'running'), (40, 'paused'), (50, 'cancelled'), (60, 'done')], default=10)),
                ('date_added', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prodsys.Task'),
        ),
    ]
