from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from core.models import APIKey


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.META.get("HTTP_X_API_KEY")
        if not api_key:
            return None

        try:
            api_key_obj = APIKey.objects.get(key=api_key)
            return (None, None)
            # return (api_key_obj.user, None)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed("Invalid API Key")
