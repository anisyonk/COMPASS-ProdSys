# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-07 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodsys', '0049_auto_20170906_2034'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='job',
            name='prodsys_job_task_id_a3b4c0_idx',
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.CharField(choices=[('test production', 'test production'), ('mass production', 'mass production'), ('DDD filtering', 'DDD filtering')], default='test production', max_length=50),
        ),
    ]
