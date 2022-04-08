from rest_framework import viewsets

from accounts.models import UserRoutine, User
from accounts.serializers import UserRoutineSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRoutineViewSet(viewsets.ModelViewSet):
    queryset = UserRoutine.objects.all()
    serializer_class = UserRoutineSerializer