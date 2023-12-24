from django.contrib.auth import get_user_model, login

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION", "")
        if auth_header.startswith("Bearer "):
            api_key = auth_header.split("Bearer ")[1]
        else:
            print("No API Key")
            raise AuthenticationFailed("No API Key provided")
        try:
            user = get_user_model().objects.get(apikey=api_key)
            return (user, api_key)
        except get_user_model().DoesNotExist:
            raise AuthenticationFailed("Invalid API Key")
