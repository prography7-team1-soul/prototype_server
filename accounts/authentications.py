from rest_framework.authentication import BaseAuthentication
from accounts.models import User


class UuidAuthentication(BaseAuthentication):

    def authenticate(self, request):
        headers = request.headers
        uuid = headers.get("uuid", None)

        if uuid is None:
            return None

        user = User.objects.get(uuid=uuid)
        return (user, None)