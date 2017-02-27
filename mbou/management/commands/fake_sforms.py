from django.core.management.base import BaseCommand, CommandError

from mbou.models import StudyForm

class Command(BaseCommand):
  help = "creates fake forms"

  def handle(self, *args, **options):
    number = 11
    for i in range(1, number):
      frm = StudyForm()
      frm.number = i
      frm.designator = u"а"
      frm.save()
      self.stdout.write("[%d] added studyform %s" % (i, str(frm)))
