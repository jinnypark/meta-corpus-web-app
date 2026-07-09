"""

Production settings for *****

"""

from .base import *  # pylint: disable=unused-wildcard-import, wildcard-import

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']  # set in venv activate

ADMINS = [('Jinny Park', 'jinnyparkmus@gmail.com')]  # Django will email this address on internal server errors

# Fly.io's internal health checks hit the machine directly over its private
# network using the machine's own IP as the Host header (not the public
# meta-corpus-web-app.fly.dev hostname), so a fixed allowlist would reject
# them. The app is only reachable from the internet through Fly's edge
# proxy, which is what actually gates external access here.
ALLOWED_HOSTS = ['*']

CORS_ORIGIN_WHITELIST = []

# the deployment platform (Fly.io) terminates TLS at its edge proxy and
# forwards plain HTTP internally, flagging the original scheme via this
# header -- without it Django can't tell the request was actually HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# db.sqlite3 and the PDF render cache need to live on a persistent volume,
# not the container's ephemeral filesystem -- DATA_DIR is that volume's
# mount point (see fly.toml)
DATA_DIR = os.environ.get('DATA_DIR', BACKEND_DIR)

DATABASES['default']['NAME'] = os.path.join(DATA_DIR, 'db.sqlite3')
MEDIA_ROOT = os.path.join(DATA_DIR, 'files/')

# serve static files (the frontend bundle, logos) directly from gunicorn --
# no separate nginx/CDN needed at this scale. Must go immediately after
# SecurityMiddleware (index 2 in base.py's MIDDLEWARE), per whitenoise's
# own setup docs.
MIDDLEWARE.insert(3, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
