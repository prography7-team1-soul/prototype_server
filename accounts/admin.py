from django.contrib import admin

# Register your models here.
from accounts.models import ImitatedUser, User

admin.site.register([User,ImitatedUser])