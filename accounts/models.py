from django.db import models

class User(models.Model):
    uuid = models.CharField(max_length=65)

    def __str__(self):
        return self.uuid

class ImitatedUser(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    celebrity = models.ForeignKey('celebrities.Celebrity', on_delete=models.CASCADE)
    imitated_at = models.DateTimeField(auto_now_add=True)

