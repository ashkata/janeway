# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-11 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned', models.DateTimeField(default=django.utils.timezone.now)),
                ('notified', models.BooleanField(default=False)),
                ('decision', models.CharField(blank=True, choices=[('accept', 'Accept'), ('corrections', 'Corrections Required')], help_text="Select a decision that reflects your actions. If you've uploaded a newversion of the file, select Corrects Required, if you're happy with thecopyedit, select Accept.", max_length=20, null=True, verbose_name='Your Decision')),
                ('date_decided', models.DateTimeField(blank=True, null=True)),
                ('author_note', models.TextField(blank=True, null=True, verbose_name='Note to the Editor')),
            ],
        ),
        migrations.CreateModel(
            name='CopyeditAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned', models.DateTimeField(default=django.utils.timezone.now)),
                ('notified', models.BooleanField(default=False)),
                ('due', models.DateField(default=django.utils.timezone.now)),
                ('editor_note', models.TextField(blank=True, null=True, verbose_name='Note for the Copyeditor')),
                ('copyeditor_note', models.TextField(blank=True, null=True, verbose_name='Note for the Editor')),
                ('decision', models.CharField(blank=True, choices=[('accept', 'Accept'), ('decline', 'Decline')], max_length=20, null=True)),
                ('date_decided', models.DateTimeField(blank=True, null=True)),
                ('copyeditor_completed', models.DateTimeField(blank=True, null=True)),
                ('copyedit_reopened', models.DateTimeField(blank=True, null=True)),
                ('copyedit_reopened_complete', models.DateTimeField(blank=True, help_text='The date a reopen was complete', null=True)),
                ('copyedit_accepted', models.DateTimeField(blank=True, null=True)),
                ('copyedit_acknowledged', models.BooleanField(default=False)),
            ],
        ),
    ]
