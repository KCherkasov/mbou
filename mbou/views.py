from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from photologue.models import Photo, Gallery

from django.utils import timezone
import re

from mbou.models import News, StudyForm, LessonTiming, Schedule, Document, DocumentCategory
from mbou.forms import AddNewsForm, StudyFormForm, LessonTimingForm, ScheduleForm, DocumentForm, PhotoAddForm, GalleryAddForm

from mbou import miscellaneous

from photologue import views

def index(request):
  return render(request, 'index.html', { "news": News.objects.all, 'year' : timezone.now,  "cats" : DocumentCategory.objects.get_top_X, })

def base(request):
  return render(request, 'base.html', {})

def news(request, id):
  try:
    news = News.objects.get(pk = int(id))
  except News.DoesNotExist:
    raise Http404()
  return render(request, "news_one.html", { "n": news, "news": News.objects.all, "year": timezone.now, "cats" : DocumentCategory.objects.get_top_X, })

def news_add(request):
  if request.method == 'POST':
    add = News()
    form = AddNewsForm(request.POST, instance = add)
    if (form.is_valid()):
      added = form.save()
      return HttpResponseRedirect(reverse('news', kwargs = {'id' : added.id,}))
  else:
    form = AddNewsForm()
  return render(request, 'news_add.html', { 'form' : form, "news": News.objects.all, "year": timezone.now, "cats" : DocumentCategory.objects.get_top_X, })

def lesson_edit(request):
  if request.method == "POST":
    form = LessonTimingForm(request.POST)
    if (form.is_valid()):
      form.save()
      return HttpResponseRedirect(reverse('lessons_show'))
    else:
      form = LessonTimingForm(request.POST)
      return render(request, 'lesson_edit.html', { 'form' : form, 'news': News.objects.all, "year": timezone.now, "cats" : DocumentCategory.objects.get_top_X, })
  else:
    form = LessonTimingForm()
  return render(request, 'lesson_edit.html', { 'form' : form, 'news': News.objects.all, "year": timezone.now, "cats" : DocumentCategory.objects.get_top_X, })

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
    return render(request, 'schedule_edit.html', { 'form' : form, 'news' : News.objects.all, "year": timezone.now, 'les1' : lesson1, 'les2' : lesson2, 'les3' : lesson3, 'les4' : lesson4, 'les5' : lesson5, 'les6' : lesson6, 'les7' : lesson7, 'les8' : lesson8, "cats" : DocumentCategory.objects.get_top_X, })

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
  return render(request, 'schedule_show.html', { 'sform_no': sform_no, 'scheds' : scheds, 'news' : News.objects.all, "year": timezone.now, 'les1' : lesson1, 'les2' : lesson2, 'les3' : lesson3, 'les4' : lesson4, 'les5' : lesson5, 'les6' : lesson6, 'les7' : lesson7, 'les8' : lesson8, "cats" : DocumentCategory.objects.get_top_X, })

def lessons_show(request):
  lessons = LessonTiming.objects.all().order_by('number')
  return render(request, 'lessons_show.html', { 'lessons' : lessons, 'news' : News.objects.all, "year": timezone.now, "cats" : DocumentCategory.objects.get_top_X, })

def document_show(request, title):
  try:
    doc = Document.objects.get_by_title(title);
  except Document.DoesNotExist:
    raise Http404()
  doc_namext = re.split('[.]+', doc.doc.name)
  if doc_namext[1] == 'pdf':
    is_pdf = True
  else:
    is_pdf = False
  return render(request, "document.html", { 'doc' : doc, 'news' : News.objects.all, 'year' : timezone.now, 'categories' : DocumentCategory.objects.order_by_doc_count().all, "cats" : DocumentCategory.objects.get_top_X, 'is_pdf' : is_pdf} )

def document_add(request):
   if request.method == 'POST':
     form = DocumentForm(request.POST, request.FILES);
     if form.is_valid():
       added = form.save()
       return HttpResponseRedirect(reverse('document_show', kwargs = { 'title' : added.title_id, }))
   else:
     form = DocumentForm()
   return render(request, "document_add.html", { 'form' : form, 'news' : News.objects.all, 'year' : timezone.now, "cats" : DocumentCategory.objects.get_top_X, })

def docs_newest(request):
  documents = Document.objects.newest()
  pagination = miscellaneous.paginate(documents, request, key='document')
  return render(request, 'docs_list.html', { 'title' : u'Новые документы', 'news' : News.objects.all, 'year' : timezone.now, 'docs' : pagination, 'categories' : DocumentCategory.objects.order_by_doc_count().all, "cats" : DocumentCategory.objects.get_top_X,  })

def docs_by_category(request, cat_name):
  try:
    cat_obj = DocumentCategory.objects.get_by_name_id(cat_name)
  except DocumentCategory.DoesNotExist:
    raise Http404()
  documents = Document.objects.by_category(cat_obj)
  pagination = miscellaneous.paginate(documents, request, key='document')
  return render(request, 'docs_list.html', { 'title' : u'Новые документы', 'news' : News.objects.all, 'year' : timezone.now, 'docs' : pagination, 'categories' : DocumentCategory.objects.order_by_doc_count().all, "cats" : DocumentCategory.objects.get_top_X, "cat_name" : cat_obj.name, })

class MbouPhotoListView(views.PhotoListView):
  def get_context_data(self, **kwargs):
    context = super(MbouPhotoListView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouPhotoDetailView(views.PhotoDetailView):
  def get_context_data(self, **kwargs):
    context = super(MbouPhotoDetailView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouPhotoDateView(views.PhotoDateView):
  def get_context_data(self, **kwargs):
    context = super(MbouPhotoDateView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouPhotoDateDetailView(views.PhotoDateDetailView):
  def get_context_data(self, **kwargs):
    context = super(MbouPhotoDateDetailView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouPhotoArchiveIndexView(views.PhotoArchiveIndexView):
  def get_context_data(self, **kwargs):
    context = super(MbouPhotoArchiveIndexView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouPhotoDayArchiveView(views.PhotoDayArchiveView):
  def get_context_data(self, **kwargs):
    context = super(MbouPhotoDayArchiveView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouPhotoMonthArchiveView(views.PhotoMonthArchiveView):
  def get_context_data(self, **kwargs):
    context = super(MbouPhotoMonthArchiveView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouPhotoYearArchiveView(views.PhotoYearArchiveView):
  def get_context_data(self, **kwargs):
    context = super(MbouPhotoYearArchiveView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouGalleryListView(views.GalleryListView):
  def get_context_data(self, **kwargs):
    context = super(MbouGalleryListView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouGalleryDetailView(views.GalleryDetailView):
  def get_context_data(self, **kwargs):
    context = super(MbouGalleryDetailView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouGalleryDateView(views.GalleryDateView):
  def get_context_data(self, **kwargs):
    context = super(MbouGalleryDateView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouGalleryDateDetailView(views.GalleryDateDetailView):
  def get_context_data(self, **kwargs):
    context = super(MbouGalleryDateDetailView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouGalleryArchiveIndexView(views.GalleryArchiveIndexView):
  def get_context_data(self, **kwargs):
    context = super(MbouGalleryArchiveIndexView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouGalleryDayArchiveView(views.GalleryDayArchiveView):
  def get_context_data(self, **kwargs):
    context = super(MbouGalleryDayArchiveView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouGalleryMonthArchiveView(views.GalleryMonthArchiveView):
  def get_context_data(self, **kwargs):
    context = super(MbouGalleryDetailView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouGalleryYearArchiveView(views.GalleryYearArchiveView):
  def get_context_data(self, **kwargs):
    context = super(MbouGalleryDetailView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

class MbouCreateView(CreateView):
  def get_context_data(self, **kwargs):
    context = super(MbouCreateView, self).get_context_data(**kwargs)
    context['year'] = timezone.now
    context['news'] = News.objects.all
    context['cats'] = DocumentCategory.objects.get_top_X
    return context

#deprecated

class MbouGalleryCreateView(MbouCreateView):
  model = Gallery
  fields = ['title', 'slug', 'description', 'photos']

class MbouPhotoCreateView(MbouCreateView):
  model = Photo
  fields = ['title', 'slug', 'caption', 'image']

# deprecated end

def gallery_add(request):
  if request.method == 'POST':
    form = GalleryAddForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('galleries'))
  else:
    form = GalleryAddForm()
  return render(request, 'gallery_add.html', { 'form' : form, 'news': News.objects.all, "year": timezone.now, "cats" : DocumentCategory.objects.get_top_X, })

def photo_add(request):
  if request.method == 'POST':
    form = PhotoAddForm(request.POST, request.FILES)
    if  form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('photo_add'))
  else:
    form = PhotoAddForm()
  return render(request, 'photo_add.html', { 'form' : form, 'year' : timezone.now, 'news' : News.objects.all, 'cats' : DocumentCategory.objects.get_top_X, })
