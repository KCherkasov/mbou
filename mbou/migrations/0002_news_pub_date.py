# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 23:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mbou', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]