from django.db import models

class Celebrity(models.Model):
    name = models.CharField(max_length=15)
    english_name = models.CharField(max_length=31)
    image = models.ImageField()
    job = models.CharField(max_length=15)
    MBTI = models.CharField(max_length=7)
    nationality = models.CharField(max_length=15)
    introduction = models.TextField()
    body_spec = models.JSONField()
    education = models.CharField(max_length=63)
    wise_saying = models.CharField(max_length=31)
    wealth = models.CharField(max_length=63)
    spouse = models.CharField(max_length=31)
    children = models.CharField(max_length=63)
    age = models.PositiveIntegerField()
    birthday = models.CharField(max_length=31)
    deceased_at = models.CharField(max_length=31)
    celebrity_routines = models.JSONField()

    def __str__(self):
        return self.name