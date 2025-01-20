import io
import json
from django.http.response import HttpResponse, FileResponse
from music21 import converter
from scripts.converters import *
from app.models import Score

def handler_score(request, filename):
    """
    Handler for returning a score
    """
    results = Score.objects.filter(file__contains=filename)
    if results:
        row = results[0]
        score = converter.parse(row.text, format=row.format)
        temp = score.write('mxl')
        return FileResponse(open(temp, 'rb'), filename=f'{row.file}.mxl', as_attachment=True)
    else:
        return HttpResponse('no score matching the given query')


def handler_text(request, filename):
    """
    Handler for returning an annotation
    """
    results = Score.objects.filter(file__contains=filename)
    if results:
        row = results[0]
        temp = io.BytesIO(row.text.encode())
        temp.seek(0)
        return FileResponse(temp, filename=row.file, as_attachment=True)
    else:
        return HttpResponse('no score matching the given query')


def handler_facts(request, filename):
    """
    Handler for returning the factsheet as json
    """
    results = Score.objects.filter(file__contains=filename)
    if results:
        row = results[0]
        json_str = json.dumps(row.factsheet, indent=4)
        temp = io.BytesIO(json_str.encode())
        temp.seek(0)
        return FileResponse(temp, filename=f'{row.file}.json', as_attachment=True)
    else:
        return HttpResponse('no score matching the given query')