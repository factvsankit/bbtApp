# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-07 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadataapp', '0005_auto_20160801_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='nepali_event_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
