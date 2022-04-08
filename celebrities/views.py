from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from accounts.models import UserRoutine
from celebrities.models import Celebrity
from celebrities.serializers import CelebritySummarizeSerializer, CelebritySerializer


class CelebrityViewSet(ReadOnlyModelViewSet):
    queryset = Celebrity.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CelebritySummarizeSerializer
        else:
            return CelebritySerializer

    @action(detail=True, methods=['post'])
    def routines(self, request, pk):
        celebrity = Celebrity.objects.get(id=pk)
        celebrity_routines = celebrity.celebrity_routines
        for routine in celebrity_routines.items():
            UserRoutine.objects.create(content=routine, imitated_user=request.user, celebrity=celebrity)
        data = {
            'result': 'success'
        }
        return Response(data,status.HTTP_201_CREATED)