# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 05:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temple', '0003_auto_20171201_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='level',
        ),
        migrations.RemoveField(
            model_name='student',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='student',
            name='class_level',
        ),
        migrations.RemoveField(
            model_name='student',
            name='volunteer',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='Level',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Volunteer',
        ),
    ]
