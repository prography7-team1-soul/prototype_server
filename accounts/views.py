from rest_framework import viewsets

from accounts.models import UserRoutine
from accounts.serializers import UserRoutineSerializer


class UserRoutineViewSet(viewsets.ModelViewSet):
    queryset = UserRoutine.objects.all()
    serializer_class = UserRoutineSerializer