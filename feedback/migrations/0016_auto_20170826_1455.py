# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-26 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0015_auto_20170826_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_pic',
            field=models.ImageField(default='/media/pic_folder/nologo.jpg', upload_to='pic_folder/'),
        ),
    ]