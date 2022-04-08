from django.db import models

class User(models.Model):
    uuid = models.CharField(max_length=65)

    def __str__(self):
        return self.uuid

class UserRoutine(models.Model):
    content = models.JSONField()
    is_completed = models.BooleanField(default=False)
    imitated_user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    celebrity = models.ForeignKey('celebrities.Celebrity', on_delete=models.CASCADE)