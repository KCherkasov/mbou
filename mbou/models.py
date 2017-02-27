# -*- coding: utf-8 -*-
from django.db import models

import datetime
from django.utils import timezone
from django.db.models import Count, Sum

from django.core import validators
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

class News(models.Model):
  title = models.TextField()
  content = models.TextField()
  pub_date = models.DateTimeField(default = timezone.now)

  def get_by_title(self, title):
    return self.get(title = title)

  def get_by_content(self, content):
    return self.get(content = content)

  def get_by_date(self, date):
    return self.get(pub_date = date)

  def get_url(self):
    return reverse('news', kwargs={'id': self.id,})

class StudyFormManager(models.Manager):
  def get_by_number(self, number):
    return self.get(number = number)

  def get_by_designator(self, designator):
    return self.get(designator = designator)

  def get_by_full(self, number, designator):
    return self.get(number=number, designator=designator)

class StudyForm(models.Model):
  number = models.PositiveIntegerField(default = 1, validators = [ validators.MaxValueValidator(11), validators.MinValueValidator(1), ])
  designator = models.TextField()
  objects = StudyFormManager()

  def __unicode__(self):
    return str(self.number) + self.designator

  def __str__(self):
    return str(self.number) + self.designator

  def get_url(self):
    return reverse('form', kwargs={'id': self.id,})

class LessonTiming(models.Model):
  number = models.PositiveIntegerField(default = 1, validators = [ validators.MaxValueValidator(8), validators.MinValueValidator(1), ])
  start = models.TimeField()
  end = models.TimeField()


class Schedule(models.Model):
  sform = models.ForeignKey(StudyForm)
  
  monday1 = models.TextField(blank = True)
  monday2 = models.TextField(blank = True)
  monday3 = models.TextField(blank = True)
  monday4 = models.TextField(blank = True)
  monday5 = models.TextField(blank = True)
  monday6 = models.TextField(blank = True)
  monday7 = models.TextField(blank = True)
  monday8 = models.TextField(blank = True)

  tuesday1 = models.TextField(blank = True)
  tuesday2 = models.TextField(blank = True)
  tuesday3 = models.TextField(blank = True)
  tuesday4 = models.TextField(blank = True)
  tuesday5 = models.TextField(blank = True)
  tuesday6 = models.TextField(blank = True)
  tuesday7 = models.TextField(blank = True)
  tuesday8 = models.TextField(blank = True)

  wednesday1 = models.TextField(blank = True)
  wednesday2 = models.TextField(blank = True)
  wednesday3 = models.TextField(blank = True)
  wednesday4 = models.TextField(blank = True)
  wednesday5 = models.TextField(blank = True)
  wednesday6 = models.TextField(blank = True)
  wednesday7 = models.TextField(blank = True)
  wednesday8 = models.TextField(blank = True)

  thursday1 = models.TextField(blank = True)
  thursday2 = models.TextField(blank = True)
  thursday3 = models.TextField(blank = True)
  thursday4 = models.TextField(blank = True)
  thursday5 = models.TextField(blank = True)
  thursday6 = models.TextField(blank = True)
  thursday7 = models.TextField(blank = True)
  thursday8 = models.TextField(blank = True)

  friday1 = models.TextField(blank = True)
  friday2 = models.TextField(blank = True)
  friday3 = models.TextField(blank = True)
  friday4 = models.TextField(blank = True)
  friday5 = models.TextField(blank = True)
  friday6 = models.TextField(blank = True)
  friday7 = models.TextField(blank = True)
  friday8 = models.TextField(blank = True)

  def get_by_sform(self, sform):
    return self.get(sform = sform)

  
