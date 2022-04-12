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

THIRD_PARTY_APPS += [
    'corsheaders',
]

MIDDLEWARE +=[
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_WHITELIST = ['http://127.0.0.1','http://localhost']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGIN_REGEXES = ['http://127.0.0.1','http://localhost',]