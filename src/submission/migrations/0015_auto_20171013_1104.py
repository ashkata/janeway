# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 11:04
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0014_auto_20171009_1028'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('allarticles', django.db.models.manager.Manager()),
            ],
        ),
    ]
