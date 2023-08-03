"""
Views for the user API.
"""

from django.views import View
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import (
    generics,
    permissions,
)

from account.serializers import MyUserSerializer


def get_csrf_token(request):
    csrf_token = request.COOKIES.get("csrftoken")

    other_cookies = {
        "sessionid": request.COOKIES.get("sessionid"),
    }

    data = {
        "csrf_token": csrf_token,
        "other_cookies": other_cookies,
    }
    print(data)
    return JsonResponse(data)


class RedirectSocial(View):
    def get(self, request, *args, **kwargs):
        code, state = str(request.GET["code"]), str(request.GET["state"])
        json_obj = {"code": code, "state": state}
        print(json_obj)
        return JsonResponse(json_obj)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""

    serializer_class = MyUserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""

    serializer_class = MyUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return authentication user."""
        return self.request.user
