from django.db import models
from django.utils.translation import gettext_lazy as _

class Celebrity(models.Model):
    name = models.CharField(max_length=15)
    english_name = models.CharField(max_length=31)
    image = models.ImageField()
    job = models.ForeignKey('celebrities.CelebrityJob', on_delete=models.CASCADE)
    MBTI = models.CharField(max_length=7)
    nationality = models.CharField(max_length=15)
    introduction = models.TextField()
    body_spec = models.JSONField(blank=True, default=dict)
    education = models.CharField(max_length=63, blank=True, default='')
    wise_saying = models.JSONField(blank=True, default=dict)
    wealth = models.TextField(blank=True, default='')
    spouse = models.CharField(max_length=31, blank=True, default='')
    children = models.TextField(blank=True,default='')
    age = models.PositiveIntegerField(blank=True, default='')
    birthday = models.CharField(max_length=31, blank=True, default='')
    deceased_at = models.CharField(max_length=31, blank=True, default='')
    celebrity_routines = models.ManyToManyField('celebrities.CelebrityRoutine')
    tmi = models.ManyToManyField('celebrities.CelebrityTmi')

    def __str__(self):
        return self.name

class CelebrityTmi(models.Model):
    content = models.CharField(max_length=32)

class CelebrityRoutine(models.Model):
    content = models.CharField(max_length=31)
    time = models.CharField(max_length=7)

class CelebrityJob(models.Model):
    name = models.CharField(max_length=15)

    class ColorType(models.TextChoices):
        MAIN = 'soulMain', _('Main')
        SUB = 'soulSub', _('Sub')
        BLACK = 'soulBlack', _('Black')
        GRAY1 = 'soulGray1', _('Gray1')
        GRAY2 = 'soulGray2', _('Gray2')
        RED1 = 'soulRed1', _('Red1')
        RED2 = 'soulRed2', _('Red2')
        NEGATIVE = 'soulNegative', _('Negative')
        GREEN1 = 'soulGreen1', _('Green1')
        GREEN2 = 'soulGreen2', _('Green2')
        PINK1 = 'soulPink1', _('Pink1')
        PINK2 = 'soulPink2', _('Pink2')

    background_color = models.CharField(
        max_length=31,
        choices=ColorType.choices,
    )
    text_color = models.CharField(
        max_length=31,
        choices=ColorType.choices,
    )

    def __str__(self):
        return self.name