from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=15)

    def __str__(self):
        return self.nickname

class Routine(models.Model):
    content = models.CharField(max_length=31)
    is_completed = models.BooleanField(default=False)
    celebrity = models.ForeignKey('celebrities.Celebrity', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.content