# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-15 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prodsys', '0050_auto_20170907_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='prodsys.Task'),
        ),
    ]