"""

Local development Django settings for *****

Under no circumstances run the server with these settings in production!

"""

from .base import *  # pylint: disable=unused-wildcard-import, wildcard-import


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']  # set in venv activate

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []  # wildcard
