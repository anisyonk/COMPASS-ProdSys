# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-23 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodsys', '0057_auto_20171019_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status_castor',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
