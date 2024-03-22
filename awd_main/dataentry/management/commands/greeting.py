from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = 'Greets the user'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str,help='Name of the user')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f'Hello, {name}!'
        self.stdout.write(greeting)