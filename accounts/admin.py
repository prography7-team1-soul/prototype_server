from django.contrib import admin

# Register your models here.
from accounts.models import UserRoutine, User

admin.site.register([User, UserRoutine])