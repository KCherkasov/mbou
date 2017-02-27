from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse

from django.utils import timezone

from mbou.models import News, StudyForm, LessonTiming, Schedule
from mbou.forms import AddNewsForm, StudyFormForm, LessonTimingForm, ScheduleForm

def index(request):
  return render(request, 'index.html', { "news": News.objects.all, })
  
def base(request):
  return render(request, 'base.html', {})

def news(request, id):
  try:
    news = News.objects.get(pk = int(id))
  except News.DoesNotExist:
    raise Http404()
  return render(request, "news_one.html", { "n": news, "news": News.objects.all, "year": timezone.now, })

def news_add(request):
  if request.method == 'POST':
    add = News()
    form = AddNewsForm(request.POST, instance = add)
    if (form.is_valid()):
      added = form.save()
      return HttpResponseRedirect(reverse('news', kwargs = {'id' : added.id,}))
  else:
    form = AddNewsForm()
    return render(request, 'news_add.html', { 'form' : form, "news": News.objects.all, "year": timezone.now, })

def lesson_edit(request):
  if request.method == "POST":
    form = LessonTimingForm(request.POST)
    if (form.is_valid()):
      form.save()
      return HttpResponseRedirect(reverse('lessons_show'))
    else:
      form = LessonTimingForm(request.POST)
      return render(request, 'lesson_edit.html', { 'form' : form, 'news': News.objects.all, "year": timezone.now, })
  else:
    form = LessonTimingForm()
    return render(request, 'lesson_edit.html', { 'form' : form, 'news': News.objects.all, "year": timezone.now, })

def schedule_edit(request):
  lesson1 = LessonTiming.objects.get(number = 1)
  lesson2 = LessonTiming.objects.get(number = 2)
  lesson3 = LessonTiming.objects.get(number = 3)
  lesson4 = LessonTiming.objects.get(number = 4)
  lesson5 = LessonTiming.objects.get(number = 5)
  lesson6 = LessonTiming.objects.get(number = 6)
  lesson7 = LessonTiming.objects.get(number = 7)
  lesson8 = LessonTiming.objects.get(number = 8)
  if request.method == 'POST':
    add = Schedule()
    form = ScheduleForm(request.POST, instance = add)
    if (form.is_valid()):
      added = form.save()
      return HttpResponseRedirect(reverse('schedule_show', kwargs = {'sform_no' : added.sform.number}))
  else:
    form = ScheduleForm()
    return render(request, 'schedule_edit.html', { 'form' : form, 'news' : News.objects.all, "year": timezone.now, 'les1' : lesson1, 'les2' : lesson2, 'les3' : lesson3, 'les4' : lesson4, 'les5' : lesson5, 'les6' : lesson6, 'les7' : lesson7, 'les8' : lesson8, })

def schedule_show(request, sform_no):
  lesson1 = LessonTiming.objects.get(number = 1)
  lesson2 = LessonTiming.objects.get(number = 2)
  lesson3 = LessonTiming.objects.get(number = 3)
  lesson4 = LessonTiming.objects.get(number = 4)
  lesson5 = LessonTiming.objects.get(number = 5)
  lesson6 = LessonTiming.objects.get(number = 6)
  lesson7 = LessonTiming.objects.get(number = 7)
  lesson8 = LessonTiming.objects.get(number = 8)
  scheds = Schedule.objects.filter(sform__number = int(sform_no))
  if scheds != None:
    scheds.order_by('designator')
  return render(request, 'schedule_show.html', { 'sform_no': sform_no, 'scheds' : scheds, 'news' : News.objects.all, "year": timezone.now, 'les1' : lesson1, 'les2' : lesson2, 'les3' : lesson3, 'les4' : lesson4, 'les5' : lesson5, 'les6' : lesson6, 'les7' : lesson7, 'les8' : lesson8, })

def lessons_show(request):
  lessons = LessonTiming.objects.all().order_by('number')
  return render(request, 'lessons_show.html', { 'lessons' : lessons, 'news' : News.objects.all, "year": timezone.now, })
