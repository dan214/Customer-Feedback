# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 05:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_myuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='date_of_birth',
        ),
    ]
