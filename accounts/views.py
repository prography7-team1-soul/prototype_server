from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
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

    @swagger_auto_schema(operation_description="유저의 id 값을 확인하는 API")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="uuid값을 통한 회원생성 API: 헤더에 uuid값만 넣어서 request")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class UserRoutineViewSet(viewsets.ModelViewSet):
    queryset = UserRoutine.objects.all()
    serializer_class = UserRoutineSerializer

    def get_queryset(self):
        if self.action == 'list':
            return UserRoutine.objects.filter(imitated_user=self.request.user)
        else:
            return UserRoutine.objects.all()

    @swagger_auto_schema(operation_description="모방해온 루틴 각각을 삭제하는 API: id값은 imitate해온 루틴의 id")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="모방해온 루틴 전체를 반환하는 API: 헤더에 uuid값만 넣어서 request")
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        routines_serializer = self.get_serializer(queryset, many=True)
        query = queryset.first()
        celebrity_name = None
        if query:
            celebrity_name = query.celebrity
        routine_count = UserRoutine.objects.filter(imitated_user=request.user, is_completed=False).count()
        serializer = {
            'routine_count': routine_count,
            'celebrity_name': f'{celebrity_name}',
            'routines':routines_serializer.data,
        }
        return Response(serializer)

    @swagger_auto_schema(operation_description="모방해온 루틴 각각을 수정하는 API: id값은 imitate해온 루틴의 id -> is_complete 변경시 사용")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="모방해온 루틴 각각을 반환하는 API: id값은 imitate해온 루틴의 id")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="자신만의 커스텀한 일정을 생성하는 API: 헤더에 uuid값과 함께 필요데이터들을 바디에 담아서 request")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)