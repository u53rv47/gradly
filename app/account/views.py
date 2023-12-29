"""
Views for the user API.
"""

from django.views import View
from django.http import JsonResponse

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Institute,
    Industry,
    Major,
)
from account.serializers import (
    InstituteSerializer,
    IndustrySerializer,
    MajorSerializer,
)

# from account.serializers import UserCreateSerializer


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


# class CreateUserView(generics.CreateAPIView):
#     """Create a new user in the system."""

#     serializer_class = UserCreateSerializer


# class ManageUserView(generics.RetrieveUpdateAPIView):
#     """Manage the authenticated user."""

#     serializer_class = UserCreateSerializer
#     authentication_classes = [[JWTAuthentication]]
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self):
#         """Retrieve and return authentication user."""
#         return self.request.user


class InstituteViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer
    permission_classes = [IsAuthenticated]


class ReadOnlyListViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class IndustryViewSet(ReadOnlyListViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [IsAuthenticated]


class MajorViewSet(ReadOnlyListViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = [IsAuthenticated]
