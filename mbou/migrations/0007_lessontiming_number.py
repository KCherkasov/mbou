# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-20 01:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbou', '0006_lessontiming_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessontiming',
            name='number',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)]),
        ),
    ]
