# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='name',
            field=models.CharField(max_length=280),
        ),
    ]
