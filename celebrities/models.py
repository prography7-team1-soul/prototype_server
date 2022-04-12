from django.db import models
from django.utils.translation import gettext_lazy as _

class Celebrity(models.Model):
    name = models.CharField(max_length=15)
    english_name = models.CharField(max_length=31)
    image = models.ImageField()
    job = models.ManyToManyField('celebrities.CelebrityJob')
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

class CelebrityJob(models.Model):
    name = models.CharField(max_length=15)

    class ColorType(models.TextChoices):
        MAIN = 'Ma', _('Main')
        SUB = 'Su', _('Sub')
        BLACK = 'Bl', _('Black')
        GRAY1 = 'Gy1', _('Gray1')
        GRAY2 = 'Gy2', _('Gray2')
        RED1 = 'R1', _('Red1')
        RED2 = 'R2', _('Red2')
        NEGATIVE = 'Ne', _('Negative')
        GREEN1 = 'Gr1', _('Green1')
        GREEN2 = 'Gr2', _('Green2')
        PINK1 = 'P1', _('Pink1')
        PINK2 = 'P2', _('Pink2')

    background_color = models.CharField(
        max_length=3,
        choices=ColorType.choices,
    )
    text_color = models.CharField(
        max_length=3,
        choices=ColorType.choices,
    )

    def __str__(self):
        return self.name