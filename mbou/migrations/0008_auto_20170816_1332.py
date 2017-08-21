# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 10:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mbou', '0007_lessontiming_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('doc', models.FileField(upload_to='docs')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='studyform',
            name='number',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(11), django.core.validators.MinValueValidator(1)]),
        ),
    ]