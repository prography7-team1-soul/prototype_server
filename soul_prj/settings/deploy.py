from .base import *

DEBUG = False
# AWS Setting
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = '7th-team1-soul'
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Static Setting
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'soul_prj.storages.backends.s3boto.S3BotoStorage'

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
