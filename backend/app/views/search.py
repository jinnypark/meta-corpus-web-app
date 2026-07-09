from django.http.response import HttpResponse, JsonResponse
from music21 import converter, roman
from scripts.converters import *
from app.models import Score
import time

# Scores don't carry an explicit "source corpus" column, so we classify them
# by their `file` naming convention instead. Each add_scores run gives every
# corpus a distinct, unambiguous pattern (see datasets/README.md).
SOURCES = ('rs200_tdc', 'rs200_dt', 'mcgill_billboard', 'meta_pop')

def get_source(filename):
    if '/' in filename and filename.endswith('salami_chords.txt'):
        return 'mcgill_billboard'
    if filename.endswith('_tdc.har'):
        return 'rs200_tdc'
    if filename.endswith('_dt.har'):
        return 'rs200_dt'
    return 'meta_pop'

def handler(request, progression):
    """
    Endpoint testing names of files with the chord progression
    """
    start_time = time.time()
    sources_param = request.GET.get('sources')
    selected_sources = set(sources_param.split(',')) if sources_param else set(SOURCES)

    score_hits = {}
    results = Score.objects.all()
    count = 0
    total = 0
    total_hits = 0
    for row in results:
        name, factsheet = row.file, row.factsheet
        if get_source(name) not in selected_sources: continue
        total += 1
        if not factsheet: continue
        if progression in factsheet['progression']:
            count += 1
            hits = factsheet['progression'].count(progression)
            by_section = {}
            for section in factsheet.get('sections', []):
                section_hits = section['progression'].count(progression)
                if section_hits:
                    by_section[section['name']] = by_section.get(section['name'], 0) + section_hits
            if name in score_hits:
                score_hits[name]['hits'] += hits
                for section_name, section_hits in by_section.items():
                    existing = score_hits[name]['by_section']
                    existing[section_name] = existing.get(section_name, 0) + section_hits
            else:
                score_hits[name] = {
                    'hits': hits,
                    'title': row.title,
                    'composer': row.composer,
                    'by_section': by_section,
                }
            total_hits += hits

    res = {
        'time': time.time() - start_time,
        'found': count,
        'total': total,
        'hits': total_hits,
        'scores': [
            {'file': key, **val} for key, val in score_hits.items()
        ]
    }
    return JsonResponse(res)