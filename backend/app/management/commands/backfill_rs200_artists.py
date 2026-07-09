import csv
import os
from django.core.management.base import BaseCommand
from app.models import Score

# The rs200_harmony .har files themselves carry no artist metadata (unlike
# McGill Billboard's own "# artist:" header), so composer is populated from
# this separate official index instead (see datasets/rs200_harmony/README.md
# entry for provenance). A handful of filenames differ slightly in spelling
# between the index and the actual downloaded corpus; alias them explicitly
# rather than guessing via fuzzy matching.
ALIASES = {
    'georgia_on_my_miind': 'georgia_on_my_mind',
    'blue_suede_shoes_perkins': 'blue_suede_shoes',
    'brown_eyed_girl': 'brown-eyed_girl',
    'in_the_still_of_the_nite': 'in_the_still_of_the_night',
}

class Command(BaseCommand):
    help = 'Backfills composer (artist) for rs200_harmony scores from the corpus index file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--index',
            type=str,
            default=os.path.join('..', 'datasets', 'rs200_harmony', 'rs200-index.txt'),
            help='path to the tab-delimited rs200 index file',
        )

    def handle(self, *args, **options):
        artist_by_base = {}
        with open(options['index'], encoding='utf-8') as f:
            for row in csv.reader(f, delimiter='\t'):
                if not row or not row[0]:
                    continue
                base, _rank, _title, artist, *_rest = row
                artist_by_base[ALIASES.get(base, base)] = artist

        updated = 0
        unmatched = set()
        for row in Score.objects.all():
            if not (row.file.endswith('_dt.har') or row.file.endswith('_tdc.har')):
                continue
            base = row.file.rsplit('_', 1)[0]
            artist = artist_by_base.get(base)
            if artist is None:
                unmatched.add(base)
                continue
            if row.composer != artist:
                row.composer = artist
                row.save()
                updated += 1

        print(f'{updated} scores updated with an artist name.')
        if unmatched:
            print(f'{len(unmatched)} rs200 files had no matching index entry:')
            for base in sorted(unmatched):
                print(' -', base)
