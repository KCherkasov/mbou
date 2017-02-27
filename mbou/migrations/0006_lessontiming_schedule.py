# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 23:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mbou', '0005_auto_20170119_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonTiming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday1', models.TextField(blank=True)),
                ('monday2', models.TextField(blank=True)),
                ('monday3', models.TextField(blank=True)),
                ('monday4', models.TextField(blank=True)),
                ('monday5', models.TextField(blank=True)),
                ('monday6', models.TextField(blank=True)),
                ('monday7', models.TextField(blank=True)),
                ('monday8', models.TextField(blank=True)),
                ('tuesday1', models.TextField(blank=True)),
                ('tuesday2', models.TextField(blank=True)),
                ('tuesday3', models.TextField(blank=True)),
                ('tuesday4', models.TextField(blank=True)),
                ('tuesday5', models.TextField(blank=True)),
                ('tuesday6', models.TextField(blank=True)),
                ('tuesday7', models.TextField(blank=True)),
                ('tuesday8', models.TextField(blank=True)),
                ('wednesday1', models.TextField(blank=True)),
                ('wednesday2', models.TextField(blank=True)),
                ('wednesday3', models.TextField(blank=True)),
                ('wednesday4', models.TextField(blank=True)),
                ('wednesday5', models.TextField(blank=True)),
                ('wednesday6', models.TextField(blank=True)),
                ('wednesday7', models.TextField(blank=True)),
                ('wednesday8', models.TextField(blank=True)),
                ('thursday1', models.TextField(blank=True)),
                ('thursday2', models.TextField(blank=True)),
                ('thursday3', models.TextField(blank=True)),
                ('thursday4', models.TextField(blank=True)),
                ('thursday5', models.TextField(blank=True)),
                ('thursday6', models.TextField(blank=True)),
                ('thursday7', models.TextField(blank=True)),
                ('thursday8', models.TextField(blank=True)),
                ('friday1', models.TextField(blank=True)),
                ('friday2', models.TextField(blank=True)),
                ('friday3', models.TextField(blank=True)),
                ('friday4', models.TextField(blank=True)),
                ('friday5', models.TextField(blank=True)),
                ('friday6', models.TextField(blank=True)),
                ('friday7', models.TextField(blank=True)),
                ('friday8', models.TextField(blank=True)),
                ('sform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbou.StudyForm')),
            ],
        ),
    ]