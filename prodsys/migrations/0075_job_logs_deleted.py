# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-03 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodsys', '0074_job_chunk_number_merging_histos'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='logs_deleted',
            field=models.CharField(default='no', max_length=5),
        ),
    ]