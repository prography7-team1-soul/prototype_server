from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserRoutineViewSet, UserViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r'user', UserViewSet, basename='users')
routine_router = DefaultRouter(trailing_slash=False)
routine_router.register(r'routines', UserRoutineViewSet, basename='user_routines')

urlpatterns = [
    path("", include(router.urls)),
    path("imitated/", include(routine_router.urls)),
]