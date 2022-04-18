from django.db import models

class User(models.Model):
    uuid = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.uuid

class UserRoutine(models.Model):
    content = models.CharField(max_length=31)
    time = models.CharField(max_length=7)
    is_completed = models.BooleanField(default=False)
    imitated_user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    celebrity = models.ForeignKey('celebrities.Celebrity', on_delete=models.CASCADE)

    @property
    def celebrity_name(self):
        return self.celebrity.name

    @property
    def imitated_user_name(self):
        return self.imitated_user