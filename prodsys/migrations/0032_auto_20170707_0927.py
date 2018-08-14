# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-07 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodsys', '0031_auto_20170707_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='attempt_merging_evntdmp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='attempt_merging_histos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='chunk_number_merging_evntdmp',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='job',
            name='chunk_number_merging_histos',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='job',
            name='panda_id_merging_evntdmp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='panda_id_merging_histos',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='status_merging',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='status_merging_evntdmp',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='status_merging_histos',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]