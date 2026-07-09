import os, sys
from django.core.management.base import BaseCommand
from app.models import Score
from scripts.converters import *
from scripts.factsheet import score_factsheet
from music21 import converter

class Command(BaseCommand):
    help = 'Add scores from the given directory to the database.'

    def add_arguments(self, parser):
        parser.add_argument('src', 
            type=str,
            help='a directory containing scores to be added'
        )
        parser.add_argument('ext',
            type=str,
            help='the file extensions of the files'
        )
        parser.add_argument('fmt',
            type=str,
            help='the annotation format used in the files'
        )

    def handle(self, *args, **options):
        src = options['src']
        ext = options['ext']
        fmt = options['fmt']
        error_count = 0
        added_count = 0
        # walk recursively so datasets shipped as one folder per song
        # (e.g. McGill Billboard's `<id>/salami_chords.txt` layout) are
        # picked up as well as a flat directory of files
        for dirpath, _dirnames, filenames in os.walk(src):
            for filename in filenames:
                # only upload files with specified extension
                if not filename.endswith(ext):
                    continue
                relpath = os.path.relpath(os.path.join(dirpath, filename), src)
                print('adding file:', relpath)
                with open(os.path.join(dirpath, filename), 'r') as f:
                    contents = f.read()
                    try:
                        # parse into music21 to check that can be processed
                        score = converter.parse(contents, format=fmt)
                        print('conversion successful')
                        entry = Score(
                            file=relpath,
                            title=score.metadata.title,
                            composer=score.metadata.composer if score.metadata.composer else '',
                            format=fmt,
                            text=contents,
                            factsheet=score_factsheet(score)
                        )
                        entry.save()
                        added_count += 1
                        print('added file to database:', relpath)
                    except:
                        error_count += 1
                        print('there was an error importing file:', relpath, sys.exc_info()[1])
        print(f'{added_count} scores were added to the database.')
        if error_count:
            print(f'There was an error importing {error_count} files.')
        else:
            print('All files imported successfully.')