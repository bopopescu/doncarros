# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-30 04:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_car_zip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='zip',
        ),
    ]