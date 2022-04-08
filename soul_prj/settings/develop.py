from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MIDDLEWARE += [
    'accounts.middleware.UuidMiddleWare',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'accounts.authentications.UuidAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}