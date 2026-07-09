import csv
import os
import re
from django.core.management.base import BaseCommand
from app.models import Score

# Two titles in aggregate_dataset.csv are shared by two different songs by
# different artists ("Burn": Ellie Goulding vs. Usher; "Secrets": OneRepublic
# vs. The Weeknd), so a plain title lookup is ambiguous for them. Only one
# side of each pair ever made it into the database (see datasets/README.md);
# resolve them explicitly by filename instead of guessing.
#
# el_perdon.har's title ("El perdon (forgiveness)") doesn't normalize-match
# its CSV row's title ("El perd—n (Forgiveness)") because the CSV's own
# encoding is corrupted there (an accented o became an em dash) -- alias it
# directly rather than trying to fuzzy-match mangled text. Note this is a
# duplicate of the separately-existing auto-converted
# el_perd_n_forgiveness_nicky_jam_and_enrique_iglesias.har (same song, same
# CSV row) that a future cleanup pass may want to de-duplicate.
FILE_OVERRIDES = {
    'burn.har': 'Ellie Goulding',
    'secrets_onerepublic.har': 'OneRepublic',
    'secrets_theweeknd.har': 'The Weeknd',
    'el_perdon.har': 'Nicky Jam and Enrique Iglesias',
}

def norm(title):
    return re.sub(r'[^a-z0-9]', '', title.lower())

def clean_artist(artist):
    # aggregate_dataset.csv has some mojibake (mis-decoded accented/non-ASCII
    # characters) in a handful of Artist values -- strip the stray artifacts
    # rather than leave garbled text in composer.
    artist = artist.replace('Â', '').replace('\xa0', ' ')
    return re.sub(r'\s+', ' ', artist).strip()

class Command(BaseCommand):
    help = 'Backfills composer (artist) for meta-pop-corpus scores from aggregate_dataset.csv'

    def add_arguments(self, parser):
        parser.add_argument(
            '--csv',
            type=str,
            default=os.path.join('..', 'datasets', 'meta-pop-corpus', 'aggregate_dataset.csv'),
            help='path to aggregate_dataset.csv',
        )

    def handle(self, *args, **options):
        artist_by_title = {}
        ambiguous_titles = set()
        with open(options['csv'], encoding='cp1252') as f:
            for row in csv.DictReader(f):
                key = norm(row['title'])
                artist = clean_artist(row['Artist'])
                if key in artist_by_title and artist_by_title[key] != artist:
                    ambiguous_titles.add(key)
                artist_by_title[key] = artist
        for key in ambiguous_titles:
            del artist_by_title[key]

        updated = 0
        unmatched = set()
        for row in Score.objects.all():
            # skip rs200 (_dt.har/_tdc.har) and mcgill billboard (nested path) scores
            if row.file.endswith('_dt.har') or row.file.endswith('_tdc.har'):
                continue
            if '/' in row.file:
                continue

            artist = FILE_OVERRIDES.get(row.file) or artist_by_title.get(norm(row.title))
            if artist is None:
                unmatched.add(row.file)
                continue
            if row.composer != artist:
                row.composer = artist
                row.save()
                updated += 1

        print(f'{updated} scores updated with an artist name.')
        if unmatched:
            print(f'{len(unmatched)} meta-pop-corpus files had no matching artist:')
            for fname in sorted(unmatched):
                print(' -', fname)
