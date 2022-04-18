from drf_yasg.utils import swagger_auto_schema
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
        elif self.action == "imitate":
            return ImitateRoutineSerializer
        else:
            return CelebritySerializer

    @swagger_auto_schema(operation_description="전체 유명인의 목록을 반환하는 API(메인페이지)")
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        res = {
            'celebrity_information_list': serializer.data
        }
        return Response(res)

    @swagger_auto_schema(operation_description="해당 유명인의 정보를 가져오는 API(상세페이지): id값은 해당 유명인의 id값")
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        res = {
            'celebrity_information': serializer.data
        }
        return Response(res)

    @swagger_auto_schema(operation_description="해당 유명인의 루틴의 목록을 내 루틴 목록으로 가져오는 API(살아보기 버튼 클릭시): 헤더의 uuid값 필수로 있어야함!,id값은 해당 유명인의 id값")
    @action(detail=True, methods=['post'])
    def imitate(self, request, pk):
        celebrity = Celebrity.objects.get(id=pk)
        user_routines = UserRoutine.objects.filter(imitated_user=request.user).first()
        serializer = ImitateRoutineSerializer(data=request.data, context={'request': request, 'pk': pk, 'celebrity':celebrity, 'user_routines':user_routines})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)