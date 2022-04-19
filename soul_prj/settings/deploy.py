from .base import *

DEBUG = True
# AWS Setting
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = '7th-team1-soul'
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (
    AWS_STORAGE_BUCKET_NAME, AWS_REGION)

# Static Setting
AWS_DEFAULT_ACL = None
AWS_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'soul_prj.storages.MediaStorage'


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
    'storages',
]

MIDDLEWARE +=[
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_WHITELIST = ['http://127.0.0.1','http://localhost']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGIN_REGEXES = ['http://127.0.0.1','http://localhost',]
