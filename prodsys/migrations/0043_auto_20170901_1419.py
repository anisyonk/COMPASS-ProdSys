# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-01 14:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prodsys', '0042_job_chunk_number_merging_mdst'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='job',
            unique_together=set([('task', 'file')]),
        ),
    ]
