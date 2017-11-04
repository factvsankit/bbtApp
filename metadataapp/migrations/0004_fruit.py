# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-01 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadataapp', '0003_remove_plant_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=60)),
                ('unique_name', models.CharField(blank=True, default='', max_length=40)),
                ('detailURL', models.CharField(blank=True, default='', max_length=100)),
                ('image', models.CharField(blank=True, default='', max_length=30)),
                ('last_changed_by', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]