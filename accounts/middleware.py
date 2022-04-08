from rest_framework.permissions import SAFE_METHODS
from .models import User
from django.core.exceptions import PermissionDenied

class UuidMiddleWare(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if (
            "admin" not in request.path
            and "swagger" not in request.path
        ):

            headers = request.headers
            uuid = headers.get("uuid", None)
            if not uuid:
                raise PermissionDenied()
            user = User.objects.get_or_create(uuid=uuid)
            user
        response = self.get_response(request)
        return response