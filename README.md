# Meta Popular Music Corpus Project

![](https://github.com/jinnypark/meta-corpus-web-app/blob/main/frontend-search.png)
This project is part of the [AFUP program](https://web.archive.org/web/20210510194430/https://digitalhumanities.mit.edu/calls/) in the [MIT Programs in Digital Humanities](https://digitalhumanities.mit.edu), led by Jinny Park, a former Affiliated Artist in Music and Theater Arts at MIT.
This project was done in collaboration with MIT UROP students, Kailas Kahler and Nailah Smith.

Popular Music Corpus Project connects existing symbolic datasets of popular music into a searchable, web-based database. Currently, publicly available popular music datasets are in many different formats, ranging from an excel spreadsheet to .musicXML, .krn, or even a text file that must be compiled through a C program. Many music scholars without a programming background cannot access these datasets, which prevents further scholarly discussion. Furthermore, relevant metadata of each songs—artist name, title, release date, producer names—are often missing, or inconsistently spelled. Harmonic data in these datasets are often encoded differently, which can result in conflicting analysis of the same repertoire. Such conflicting also prevents comparing or searching existing datasets efficiently.

UROPs worked with Jinny Park on automation of spell-checking metadata and updating missing metadata, querying MusicBrainz unique ID for each song based on artist name and song title. This project aims to culminate in an interactive website, where anyone can browse the database with a user-friendly interface, along with a public API that researchers can use.

## Getting started (backend)

The Django backend needs a `DJANGO_SECRET_KEY` environment variable — it's never committed to the repo, so you'll need to generate your own after cloning.

```sh
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
```

Generate a random key:

```sh
python3 -c "import secrets; chars='abcdefghijklmnopqrstuvwxyz0123456789!@#\$%^&*(-_=+)'; print(''.join(secrets.choice(chars) for _ in range(50)))"
```

Add it to the bottom of `backend/venv/bin/activate` (this file is gitignored, so it stays local) so it's exported automatically every time you activate the venv:

```sh
echo "export DJANGO_SECRET_KEY='<paste-generated-key-here>'" >> venv/bin/activate
```

Re-activate the venv to pick it up, then run the server:

```sh
source venv/bin/activate
python manage.py migrate
python manage.py runserver
```

## Getting started (frontend)

The Django backend renders the pages, but it serves a JavaScript bundle that Webpack has to build first — there's no separate frontend dev server to run day-to-day.

```sh
cd frontend
npm install
npm run build
```

`npm run build` writes the compiled bundle to `build/bundles` at the project root and a `webpack-stats.json` manifest that Django reads to find it (see `django-webpack-loader` in `backend/config/settings/base.py`). Re-run `npm run build` after any frontend change — the backend won't pick up new frontend code until you do.

(`npm start` also works and launches Webpack's dev server, but it's only useful for isolated component work — the app's pages are mounted via a script Django injects into `backend/templates/index.html`, so `npm start`'s own page won't render a working view on its own.)

## Running the app locally

With both pieces set up:

```sh
# 1. build the frontend (repeat after any frontend change)
cd frontend && npm run build

# 2. run the backend, which serves the built frontend + API
cd ../backend
source venv/bin/activate
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/`.

## Adding scores

If you already have a folder full of scores, you can bulk-import all of them in a single command — the management command scans the whole directory and reports how many succeeded and failed:

```sh
python manage.py add_scores <directory> <extension> <format>
```

- `<directory>` — the folder of annotation files to import (every matching file in it is imported in one run)
- `<extension>` — the file extension to look for (e.g. `txt`), so you can point it at a folder containing other files too
- `<format>` — the annotation format, passed to [music21](https://www.music21.org/music21docs/)'s parser

This project registers two custom formats, in `backend/scripts/converters.py`, that music21 doesn't support natively — use whichever matches the corpus you have:

| Your files are... | `<extension>` | `<format>` |
| --- | --- | --- |
| [McGill Billboard](https://ddmal.music.mcgill.ca/research/billboard/) chord annotations (metadata header + `\|`-delimited chord sections per line) | `txt` | `billboard` |
| Rolling Stone / Clercq-Temperley Roman-numeral annotations | `har` | `rs` |

Example McGill Billboard file:

```
# title: Example Song
# artist: Example Artist
# metre: 4/4
# tonic: C

verse| C:maj | G:maj | A:min | F:maj |
```

Any other music21-supported format (e.g. plain `musicxml`, `humdrum`/`.krn`) will also work with `add_scores`, but only if the files already carry Roman-numeral/chord analysis — the two formats above are the ones this project knows how to derive that from automatically (key-finding and chord-to-Roman-numeral conversion happen in `backend/scripts/jp_format.py`).

For each file, the command parses it with music21, builds a JSON "factsheet" of its chord progression (`backend/scripts/factsheet.py`), and saves it to the database. Files that fail to parse are skipped and reported in the summary at the end, so you can fix and re-run just those.

If you change how factsheets are generated, regenerate them for scores already in the database with:

```sh
python manage.py remake_factsheets
```

## Searching by chord progression

The search page (`frontend/src/search/index.js`) hits `GET /api/search/<progression>` (`backend/app/views/search.py`), which does a substring match against each score's Roman-numeral progression string (e.g. `I-V-vi-IV`) and returns which scores matched and how many times.

Once you have scores loaded, try searching for a short progression fragment like `V-vi` or `IV-I` from the search page — it matches as a plain substring, so partial progressions work too.

Individual scores can also be fetched directly:

- `GET /api/score/<filename>` — the score as a downloadable `.mxl` file
- `GET /api/score/text/<filename>` — the original annotation text
- `GET /api/score/facts/<filename>` — the generated JSON factsheet

Screenshots of the backend, and generated score and factsheet

![](https://github.com/jinnypark/meta-corpus-web-app/blob/main/backend-scores.jpeg)
![](https://github.com/jinnypark/meta-corpus-web-app/blob/main/json_factsheet.png)
![](https://github.com/jinnypark/meta-corpus-web-app/blob/main/score-xml.png)
