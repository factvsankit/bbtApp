# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-30 23:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadataapp', '0002_auto_20160730_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='events',
        ),
    ]
