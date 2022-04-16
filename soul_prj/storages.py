from storages.backends.s3boto3 import S3Boto3Storage

__all__ = (
    'S3StaticStorage',
)


# for static
class S3StaticStorage(S3Boto3Storage):
    default_acl = 'public-read'
    location = 'static'
