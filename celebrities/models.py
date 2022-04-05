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

    def __str__(self):
        return self.name

class Routine(models.Model):
    description = models.CharField()
    time = models.CharField()
    is_complete = models.BooleanField()
    celebrity = models.ForeignKey('celebrities.Celebrity', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.time