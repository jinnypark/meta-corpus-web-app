from django.http.response import HttpResponse, JsonResponse
from music21 import converter, roman
from scripts.converters import *
from app.models import Score
import time

def handler(request, progression):
    """
    Endpoint testing names of files with the chord progression
    """
    start_time = time.time()
    score_hits = {}
    results = Score.objects.all()
    count = 0
    total = 0
    total_hits = 0
    for row in results:
        total += 1
        name, factsheet = row.file, row.factsheet
        if not factsheet: continue
        if progression in factsheet['progression']:
            count += 1
            hits = factsheet['progression'].count(progression)
            if name in score_hits:
                score_hits[name] += hits 
            else:
                score_hits[name] = hits
            total_hits += hits 

    res = {
        'time': time.time() - start_time,
        'found': count,
        'total': total,
        'hits': total_hits,
        'scores': [{'file': key, 'hits': score_hits[key]} for key in score_hits]
    }
    return JsonResponse(res)