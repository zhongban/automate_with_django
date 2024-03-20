from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Greets the user'

    def handle(self, *args, **kwargs):
        self.stdout.write('Hello, world!')