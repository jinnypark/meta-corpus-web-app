import os, sys
from django.core.management.base import BaseCommand
from app.models import Score
from scripts.converters import *
from scripts.factsheet import score_factsheet
from music21 import converter

class Command(BaseCommand):
    help = 'Remakes the factsheets for all of scores in the database'

    def handle(self, *args, **options):
        errors = 0
        count = 0
        for row in Score.objects.all():
            try: 
                # parse into music21 to check that can be processed
                count += 1
                score = converter.parse(row.text, format=row.format)
                print('conversion successful')
                row.factsheet = score_factsheet(score)
                row.save()
                print('remade factsheet for:', row.file)
            except:
                print('there was an error remaking factsheet:', row.file, sys.exc_info()[1]) 
                errors += 1
        print(f'there were {errors} errors remaking the {count} factsheets.') 