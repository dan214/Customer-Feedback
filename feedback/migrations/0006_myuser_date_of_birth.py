# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_auto_20170607_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
