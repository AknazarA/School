from django.core.management.base import BaseCommand, CommandError
from school_app.models import Teacher

class Command(BaseCommand):

    def handle(self, *args, **options):
        Teacher.objects.create_superuser(phone='123456789', password='123456789')