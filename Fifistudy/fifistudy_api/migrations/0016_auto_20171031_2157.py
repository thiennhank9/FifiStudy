# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifistudy_api', '0015_fifiuser_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='video',
            field=models.FileField(upload_to=b'episode/video/'),
        ),
    ]
