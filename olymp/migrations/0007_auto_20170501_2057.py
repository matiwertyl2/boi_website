# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 20:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olymp', '0006_taskfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='solution',
        ),
        migrations.RemoveField(
            model_name='task',
            name='spoiler',
        ),
        migrations.RemoveField(
            model_name='task',
            name='statement',
        ),
        migrations.RemoveField(
            model_name='task',
            name='tests',
        ),
    ]