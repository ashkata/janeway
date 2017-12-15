# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preprint', '0008_auto_20171013_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='enabled',
            field=models.BooleanField(default=True, help_text='If disabled, this subject will not appear publicly.'),
        ),
    ]
