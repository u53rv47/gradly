from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

from chatapi.authentication import APIKeyAuthentication

from drf_spectacular.extensions import OpenApiAuthenticationExtension


class GradlyAuthentication(JWTAuthentication, APIKeyAuthentication):
    def authenticate(self, request):
        try:
            jwt_user = super().authenticate(request)
            return jwt_user
        except AuthenticationFailed as jwt_error:
            try:
                api_key_user = super(JWTAuthentication, self).authenticate(request)
                return api_key_user
            except AuthenticationFailed as api_key_error:
                raise api_key_error from jwt_error


class GradlyTokenScheme(OpenApiAuthenticationExtension):
    target_class = GradlyAuthentication
    name = "GradlyAuth"

    def get_security_definition(self, auto_schema):
        return {
            "type": "tokenAuth",
            "in": "header",
            "name": "Authorization",
            "description": "Token-based authentication with required prefix 'Bearer'",
        }
