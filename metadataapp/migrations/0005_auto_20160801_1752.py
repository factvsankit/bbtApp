# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-01 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadataapp', '0004_fruit'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='year',
            field=models.CharField(blank=True, choices=[('2016', '2016'), ('2017', '2017')], max_length=4),
        ),
        migrations.AddField(
            model_name='plant',
            name='group',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=2),
        ),
    ]
