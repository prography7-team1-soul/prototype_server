from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'soul_prj.wsgi.deploy.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}