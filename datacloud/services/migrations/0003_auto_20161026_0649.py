# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_activity_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]