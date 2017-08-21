from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
import re

from django.contrib.auth.hashers import make_password

from mbou.models import News, StudyForm, LessonTiming, Schedule, Document, DocumentCategory

class AddNewsForm(forms.ModelForm):
  class Meta:
    model = News
    fields = [ 'title', 'content', ]
    widgets = {
      'title' : forms.TextInput(attrs = {'class' : 'form-control  mbou-input-wide', 'placeholder' : u'Тема новости', }),
      'content' : forms.Textarea(attrs = {'class' : 'form-control  mbou-input-wide', 'placeholder' : u'Текст новости', }),
    }
    labels = {
      'title' : u'Тема',
      'content' : u'Текст',
    }

class StudyFormForm(forms.ModelForm):
  class Meta:
    model = StudyForm
    fields = [ 'number', 'designator', ]
    widgets = {
      'number' : forms.NumberInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Номер класса', }),
      'designator' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Обозначение класса', }),
    }
    labels = {
      'number' : u'Класс',
      'designator' : u'Буква',
    }

class LessonTimingForm(forms.ModelForm):
  class Meta:
    model = LessonTiming
    fields = ['number', 'start', 'end']
    widgets = {
      'number' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Номер урока', }),
      'start' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Время начала', }),
      'end' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Время конца', }),
    }
    labels = {
      'number' : u'Урок',
      'start' : u'Начало',
      'end' : u'Конец',
    }

  def save(self):
    data = self.cleaned_data
    les, upd = LessonTiming.objects.update_or_create(number=data.get('number'), defaults={ 'start' : data.get('start'), 'end' : data.get('end'), })
    les.save()
    return les

class ScheduleForm(forms.ModelForm):
  class Meta:
    model = Schedule
    fields = [ 'sform', 'monday1', 'monday2', 'monday3', 'monday4', 'monday5', 'monday6', 'monday7', 'monday8', 'tuesday1', 'tuesday2', 'tuesday3', 'tuesday4', 'tuesday5', 'tuesday6', 'tuesday7', 'tuesday8', 'wednesday1', 'wednesday2', 'wednesday3', 'wednesday4', 'wednesday5', 'wednesday6', 'wednesday7', 'wednesday8', 'thursday1', 'thursday2', 'thursday3', 'thursday4', 'thursday5', 'thursday6', 'thursday7', 'thursday8', 'friday1', 'friday2', 'friday3', 'friday4', 'friday5', 'friday6', 'friday7', 'friday8', ]
    widgets = {
      'monday1' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'monday2' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'monday3' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'monday4' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'monday5' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'monday6' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'monday7' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'monday8' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),

      'tuesday1' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'tuesday2' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'tuesday3' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'tuesday4' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'tuesday5' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'tuesday6' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'tuesday7' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'tuesday8' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),

      'wednesday1' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'wednesday2' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'wednesday3' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'wednesday4' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'wednesday5' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'wednesday6' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'wednesday7' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'wednesday8' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),

      'thursday1' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'thursday2' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'thursday3' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'thursday4' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'thursday5' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'thursday6' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'thursday7' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'thursday8' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),

      'friday1' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'friday2' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'friday3' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'friday4' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'friday5' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'friday6' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'friday7' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
      'friday8' : forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Введите название предмета...' }),
    }
    labels = {
      'sform' : u'Класс',

      'monday1' : u'Урок 1',
      'monday2' : u'Урок 2',
      'monday3' : u'Урок 3',
      'monday4' : u'Урок 4',
      'monday5' : u'Урок 5',
      'monday6' : u'Урок 6',
      'monday7' : u'Урок 7',
      'monday8' : u'Урок 8',

      'tuesday1' : u'Урок 1',
      'tuesday2' : u'Урок 2',
      'tuesday3' : u'Урок 3',
      'tuesday4' : u'Урок 4',
      'tuesday5' : u'Урок 5',
      'tuesday6' : u'Урок 6',
      'tuesday7' : u'Урок 7',
      'tuesday8' : u'Урок 8',

      'wednesday1' : u'Урок 1',
      'wednesday2' : u'Урок 2',
      'wednesday3' : u'Урок 3',
      'wednesday4' : u'Урок 4',
      'wednesday5' : u'Урок 5',
      'wednesday6' : u'Урок 6',
      'wednesday7' : u'Урок 7',
      'wednesday8' : u'Урок 8',

      'thursday1' : u'Урок 1',
      'thursday2' : u'Урок 2',
      'thursday3' : u'Урок 3',
      'thursday4' : u'Урок 4',
      'thursday5' : u'Урок 5',
      'thursday6' : u'Урок 6',
      'thursday7' : u'Урок 7',
      'thursday8' : u'Урок 8',

      'friday1' : u'Урок 1',
      'friday2' : u'Урок 2',
      'friday3' : u'Урок 3',
      'friday4' : u'Урок 4',
      'friday5' : u'Урок 5',
      'friday6' : u'Урок 6',
      'friday7' : u'Урок 7',
      'friday8' : u'Урок 8',
    }

  def __init__(self, *args, **kwargs):
    super(ScheduleForm, self).__init__(*args, **kwargs)
    self.fields.get('sform').queryset = StudyForm.objects.order_by('designator').order_by('number')
    self.fields.get('sform').empty_label = u'Выберите класс...'
    self.fields.get('sform').widget.attrs = { 'class' : 'form-control', }

  def save(self):
    data = self.cleaned_data
    sched, upd = Schedule.objects.update_or_create(sform = data.get('sform'), defaults={ 'monday1' : data.get('monday1'), 'monday2' : data.get('monday2'), 'monday3' : data.get('monday3'), 'monday4' : data.get('monday4'), 'monday5' : data.get('monday5'), 'monday6' : data.get('monday6'), 'monday7' : data.get('monday7'), 'monday8' : data.get('monday8'), 'tuesday1' : data.get('tuesday1'), 'tuesday2' : data.get('tuesday2'), 'tuesday3' : data.get('tuesday3'), 'tuesday4' : data.get('tuesday4'), 'tuesday5' : data.get('tuesday5'), 'tuesday6' : data.get('tuesday6'), 'tuesday7' : data.get('tuesday7'), 'tuesday8' : data.get('tuesday8'), 'wednesday1' : data.get('wednesday1'), 'wednesday2' : data.get('wednesday2'), 'wednesday3' : data.get('wednesday3'), 'wednesday4' : data.get('wednesday4'), 'wednesday5' : data.get('wednesday5'), 'wednesday6' : data.get('wednesday6'), 'wednesday7' : data.get('wednesday7'), 'wednesday8' : data.get('wednesday8'), 'thursday1' : data.get('thursday1'), 'thursday2' : data.get('thursday2'), 'thursday3' : data.get('thursday3'), 'thursday4' : data.get('thursday4'), 'thursday5' : data.get('thursday5'), 'thursday6' : data.get('thursday6'), 'thursday7' : data.get('thursday7'), 'thursday8' : data.get('thursday8'), 'friday1' : data.get('friday1'), 'friday2' : data.get('friday2'), 'friday3' : data.get('friday3'), 'friday4' : data.get('friday4'), 'friday5' : data.get('friday5'), 'friday6' : data.get('friday6'), 'friday7' : data.get('friday7'), 'friday8' : data.get('friday8'), })
    sched.save()
    return sched

class DocumentForm(forms.Form):
  title = forms.CharField(widget = forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Название документа', }), label = u'Название документа', max_length = 150)
  description = forms.CharField(widget = forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Краткое описание документа (необязательно)', }), label = u'Описание документа', required = False)
  doc = forms.FileField(widget = forms.ClearableFileInput(attrs = { 'class' : 'form-control', }), label = u'Файл')
  categories = forms.CharField(widget = forms.TextInput(attrs = { 'class' : 'form-control', 'placeholder' : u'Категории документа (каждая категория начинается с #)' }), label = u'Категории')

  def save(self):
    data = self.cleaned_data
    document = Document()
    document.title = data.get('title')
    document.title_id = document.make_title_id()
    document.description = data.get('description')
    document.save()
    if (data.get('doc') is not None):
      doc_file = data.get('doc')
      doc_namext = re.split('[.]+', doc_file.name)
      document.doc.save('%s_%s.%s' % (doc_namext[0], str(document.id), doc_namext[1]), doc_file, save = True)
    document.save()
    categories_raw = data.get('categories')
    categories_raw.lower()
    categories = re.split('[#]+', categories_raw)
    for cat_name in categories:
      if cat_name is not None and cat_name != '':
        category = DocumentCategory.objects.get_or_create(name = cat_name)
        document.categories.add(category)
    return document
