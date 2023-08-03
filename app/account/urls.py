"""
URL mappings for the user API.
"""

from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    # path("create/", views.CreateUserView.as_view(), name="create"),
    # path("profile/", views.ManageUserView.as_view(), name="profile"),
    path("code", views.RedirectSocial.as_view(), name="code"),
    path("get-csrf-token", views.get_csrf_token, name="csrf"),
]


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
