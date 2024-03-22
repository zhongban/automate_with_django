from django.core.management.base import BaseCommand
from dataentry.models import Student
import csv
from django.apps import apps

class Command(BaseCommand):
    help = 'import csv'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str,help='Name of the CSV')
        parser.add_argument('model_name', type=str,help='Name of the model')



    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        for i in apps.get_app_configs():
            try:
                model = i.get_model(model_name)
            except LookupError:
                self.stdout.write(self.style.WARNING(f'Model {model_name} not found in {i.name}'))
                continue
            else:
                break
        if model is None:
            self.stdout.write(self.style.WARNING('Model not found'))
            return


        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                Student.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('data inserted successfully!'))

    