# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-25 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodsys', '0041_remove_job_chunk_number_merging_mdst'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='chunk_number_merging_mdst',
            field=models.IntegerField(default=-1),
        ),
    ]