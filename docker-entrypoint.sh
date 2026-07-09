#!/bin/sh
set -e

python backend/manage.py migrate --noinput

exec gunicorn config.wsgi:application \
    --chdir backend \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --timeout 120
