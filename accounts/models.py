from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=15)
    routines = models.ForeignKey('celebrities.Celebrity', on_delete=models.SET_NULL)

    def __str__(self):
        return self.nickname