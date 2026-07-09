import io
import json
import os
import shutil
from django.conf import settings
from django.http.response import HttpResponse, FileResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin
from music21 import converter, environment
from scripts.converters import *
from app.models import Score

PDF_CACHE_DIR = os.path.join(settings.MEDIA_ROOT, 'pdf_cache')

# common MuseScore install locations, tried if `mscore`/`musescore` isn't on PATH
MUSESCORE_CANDIDATES = [
    shutil.which('mscore'),
    shutil.which('musescore'),
    '/Applications/MuseScore 4.app/Contents/MacOS/mscore',
    '/Applications/MuseScore 3.app/Contents/MacOS/mscore',
    '/usr/bin/musescore',
]

def _configure_musescore():
    """Point music21 at a MuseScore install so it can render notation to PDF.
    Returns True if a working install was found, False otherwise."""
    env = environment.Environment()
    if env['musicxmlPath'] and os.path.exists(env['musicxmlPath']):
        return True
    for path in MUSESCORE_CANDIDATES:
        if path and os.path.exists(path):
            env['musicxmlPath'] = path
            return True
    return False

@xframe_options_sameorigin
def handler_pdf(request, filename):
    """
    Handler for returning a rendered PDF preview of a score, for embedding
    (not a download). PDFs are generated on first request via MuseScore
    (~15-20s) and cached on disk afterwards, since re-rendering on every
    request would be far too slow for interactive use.

    Overrides the project-wide X-Frame-Options: DENY (django.middleware.
    clickjacking.XFrameOptionsMiddleware) with SAMEORIGIN -- browsers
    otherwise silently refuse to render embedded PDF content at all, since
    an <embed>/<iframe> is subject to the same clickjacking protection as a
    real frame. SAMEORIGIN keeps the protection against *other* sites
    framing this response, while allowing our own /search page to embed it.
    """
    results = Score.objects.filter(file__contains=filename)
    if not results:
        return HttpResponse('no score matching the given query')
    row = results[0]

    os.makedirs(PDF_CACHE_DIR, exist_ok=True)
    cache_path = os.path.join(PDF_CACHE_DIR, f'{row.pk}.pdf')

    if not os.path.exists(cache_path):
        if not _configure_musescore():
            return HttpResponse(
                'PDF preview requires MuseScore to be installed on the server '
                '(music21 could not find an mscore/musescore executable)',
                status=503,
            )
        score = converter.parse(row.text, format=row.format)
        temp = score.write('musicxml.pdf')
        shutil.copyfile(temp, cache_path)

    return FileResponse(open(cache_path, 'rb'), content_type='application/pdf')


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