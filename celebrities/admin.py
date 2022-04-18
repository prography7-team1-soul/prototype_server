from django.contrib import admin

# Register your models here.
from celebrities.models import Celebrity, CelebrityJob, CelebrityRoutine

admin.site.register([Celebrity, CelebrityJob, CelebrityRoutine])