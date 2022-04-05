from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from accounts.models import Routine
from accounts.serializers import RoutineSerializer
from celebrities.models import Celebrity
from celebrities.serializers import CelebritySerializer


class CelebrityViewSet(ReadOnlyModelViewSet):
    queryset = Celebrity.objects.all()
    serializer_class = CelebritySerializer

    @action(detail=True, methods=['get'])
    def routines(self, request, pk):
        routines = Routine.objects.filter(celebrity__id=pk)
        serializer = RoutineSerializer(routines, many=True)
        return Response(serializer.data, status.HTTP_200_OK)