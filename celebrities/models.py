from django.db import models

class Celebrity(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField()
    job = models.CharField(max_length=15)
    MBTI = models.CharField(max_length=7)
    nationality = models.CharField(max_length=15)
    introduction = models.TextField()
    body_spec = models.JSONField()
    education = models.CharField(max_length=15)
    wealth = models.CharField(max_length=15)
    spouse = models.CharField(max_length=15)
    children = models.JSONField()
    age = models.PositiveIntegerField()
    birthday = models.CharField(max_length=15)
    deceased_at = models.CharField(max_length=15)
    imitated_users = models.ManyToManyField(
        'accounts.User',
        through='accounts.ImitateUser',
        through_fields=('user', 'celebrity'), related_name='imitated_user')
    routines = models.ManyToManyField('celebrities.Routine')

    def __str__(self):
        return self.name

class Routine(models.Model):
    content = models.CharField(max_length=31)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.content