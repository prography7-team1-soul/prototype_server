from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from accounts.models import UserRoutine
from celebrities.models import Celebrity
from celebrities.serializers import CelebritySummarizeSerializer, CelebritySerializer, ImitateRoutineSerializer


class CelebrityViewSet(ReadOnlyModelViewSet):
    queryset = Celebrity.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CelebritySummarizeSerializer
        else:
            return CelebritySerializer

    @action(detail=True, methods=['post'])
    def imitate(self, request, pk):
        celebrity = Celebrity.objects.get(id=pk)
        serializer = ImitateRoutineSerializer(data=request.data, context={'request': request, 'pk': pk, 'celebrity':celebrity})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)