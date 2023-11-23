"""
URL mappings for the user API.
"""

from django.urls import path
from account import views
from core.models import (
    Institute,
    Industry,
    Major,
)
from rest_framework.routers import DefaultRouter

app_name = "account"

router = DefaultRouter()
router.register(r"institutes", views.InstituteViewSet, basename="institutes")
router.register(r"industries", views.IndustryViewSet, basename="industries")
router.register(r"majors", views.MajorViewSet, basename="majors")

urlpatterns = [
    # path("create/", views.CreateUserView.as_view(), name="create"),
    # path("profile/", views.ManageUserView.as_view(), name="profile"),
    path("code", views.RedirectSocial.as_view(), name="code"),
    path("get-csrf-token", views.get_csrf_token, name="csrf"),
] + router.urls

"""
# dj_rest_auth important usrls

Full Blog
https://testdriven.io/blog/django-rest-auth/


from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import path


urlpatterns = [
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
]"""
