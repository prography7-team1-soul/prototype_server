from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserRoutineViewSet, UserViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'user_routines', UserRoutineViewSet, basename='user_routines')
router.register(r'user', UserViewSet, basename='users')

urlpatterns = [
    path("", include(router.urls)),
]