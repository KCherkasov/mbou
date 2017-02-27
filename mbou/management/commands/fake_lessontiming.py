from django.core.management.base import BaseCommand, CommandError
import datetime

from mbou.models import LessonTiming

class Command(BaseCommand):
  help = "creates fake timetables."

  def handle(self, *args, **options):
    number = 8
    for i in range(1, number):
      les = LessonTiming()
      if i == 1:
        les.start = datetime.time.now()
      else:
        les.start = datetime.time(LessonTiming.objects.get(id=i-1).hours, LessonTiming.objects.get(id=i-1).minutes + 15, LessonTiming.objects.get(id=i-1).seconds)
      les.end = datetime.time(les.start.hours, les.start.minutes + 45, les.start.seconds)
      les.save()
      self.stdout.write("[%d] added lessontiming %d" % (i, i))
