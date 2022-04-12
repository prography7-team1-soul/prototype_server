from .base import *

DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'soul_prj.wsgi.develop.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


