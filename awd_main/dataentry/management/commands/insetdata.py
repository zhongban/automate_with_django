from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = 'it will insert data into database'

    def handle(self, *args, **kwargs):
        Student.objects.create(roll_no='101', name='John', age=20)
        self.stdout.write(self.style.SUCCESS('data inserted successfully!'))