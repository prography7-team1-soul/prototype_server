from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from accounts.models import UserRoutine, User
from accounts.serializers import UserRoutineSerializer, UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRoutineViewSet(viewsets.ModelViewSet):
    queryset = UserRoutine.objects.all()
    serializer_class = UserRoutineSerializer

    def get_queryset(self, request):
        if self.action == 'list':
            return UserRoutine.objects.filter(imitated_user=request.user)
        else:
            return UserRoutine.objects.all()
