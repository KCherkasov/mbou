from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User

from mbou.models import News, StudyForm, Schedule, LessonTiming, Document, DocumentCategory

from random import choice, randint

class Command(BaseCommand):
  def handle(self, *args, **options):
    # lessons = Schedule.objects.all()
    # lessons.delete()
    news = News.objects.all()
    news.delete()
    docs = Document.objects.all()
    docs.delete()
    cats = DocumentCategory.objects.all()
    cats.delete()
