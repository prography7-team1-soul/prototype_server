from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserRoutineViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'user_routines', UserRoutineViewSet, basename='user_routines')

urlpatterns = [
    path("", include(router.urls)),
]