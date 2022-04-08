from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'soul_prj.wsgi.deploy.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('NAME'),
        'USER': env('USER'),
        'PASSWORD': env('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    },
}