# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='level',
            field=models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced'), ('children', 'children')], max_length=30),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='sector_name',
            field=models.CharField(choices=[('Acolyte', 'Acolyte'), ('Kitchen', 'Kitchen'), ('Dining Hall', 'Dining Hall'), ('Receptionist', 'Receptionist'), ('Tablets', 'Tablets')], max_length=50),
        ),
    ]
