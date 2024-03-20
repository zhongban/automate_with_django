from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Displays a hello world message'

    def handle(self, *args, **kwargs):
        self.stdout.write('Hello, world!')