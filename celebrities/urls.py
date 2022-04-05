from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CelebrityViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'celebrities', CelebrityViewSet, basename='celebrities')

urlpatterns = [
    path('', include(router.urls)),
]