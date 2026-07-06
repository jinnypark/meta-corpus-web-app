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

Screenshots of the backend, and generated score and factsheet

![](https://github.com/jinnypark/meta-corpus-web-app/blob/main/backend-scores.jpeg)
![](https://github.com/jinnypark/meta-corpus-web-app/blob/main/json_factsheet.png)
![](https://github.com/jinnypark/meta-corpus-web-app/blob/main/score-xml.png)
